#include "kinematics_model_generator/mcp_generator.hpp"

#include <moveit/rdf_loader/rdf_loader.h>
// ROS
// #include <ament_index_cpp/get_package_share_directory.hpp>  // for getting file path for loading
// images #include <boost/program_options.hpp>
#include <fstream>  // for reading in urdf
#include <streambuf>
// Boost
#include <boost/algorithm/string/replace.hpp>
#include <boost/algorithm/string/trim.hpp>
#include <boost/bind/bind.hpp>
#include <boost/filesystem/operations.hpp>  // for reading folders/files
#include <boost/filesystem/path.hpp>        // for reading folders/files

// Boost file system
namespace fs = boost::filesystem;

static const rclcpp::Logger LOGGER = rclcpp::get_logger("mcp_generator");

const std::string SETUP_ASSISTANT_FILE = ".setup_assistant";

MCPGenerator::MCPGenerator(rclcpp::Node::SharedPtr node) {
    config_data_ = std::make_shared<moveit_setup::DataWarehouse>(node);
    srdf_config_ = config_data_->get<moveit_setup::SRDFConfig>("srdf");
    urdf_config_ = config_data_->get<moveit_setup::URDFConfig>("urdf");

    config_data_->registerType("launches", "moveit_setup::app::LaunchesConfig");
    launches_config_ = config_data_->get<moveit_setup::app::LaunchesConfig>("launches");

    default_collisions_.initialize(node, config_data_);
    virtual_joints_.initialize(node, config_data_);
    planning_groups_.initialize(node, config_data_);

    moveit_controllers_ = std::make_shared<moveit_setup::controllers::MoveItControllers>();
    moveit_controllers_->initialize(node, config_data_);

    ros2_controllers_ = std::make_shared<moveit_setup::controllers::ROS2Controllers>();
    ros2_controllers_->initialize(node, config_data_);

    urdf_modifications_.initialize(node, config_data_);

    config_files_.initialize(node, config_data_);

    author_info_.initialize(node, config_data_);

    launch_files_.initialize(node, config_data_);
}

void MCPGenerator::loadURDFFile(const std::filesystem::path& urdf_file_path,
                                     std::vector<std::string>& xacro_args) {
    urdf_config_->loadFromPath(urdf_file_path, xacro_args);
    srdf_config_->updateRobotModel();
}

// ******************************************************************************************
// Load chosen files for creating new package
// ******************************************************************************************
bool MCPGenerator::loadNewFiles(const std::filesystem::path& urdf_file_path,
                                     std::vector<std::string>& xacro_args) {
    // Check that box is filled out
    if (urdf_file_path.empty()) {
        RCLCPP_ERROR_STREAM(LOGGER, "Error Loading Files. No robot model file specified");
        return false;
    }

    // Check that this file exits
    if (!std::filesystem::is_regular_file(urdf_file_path)) {
        RCLCPP_ERROR_STREAM(LOGGER, "Error Loading Files. Unable to locate the URDF file: "
                                        << urdf_file_path.c_str());
        return false;
    }

    try {
        loadURDFFile(urdf_file_path, xacro_args);
    } catch (const std::runtime_error& e) {
        RCLCPP_ERROR_STREAM(LOGGER, "Error Loading URDF" << e.what());
        return false;
    }

    RCLCPP_INFO(LOGGER, "Loading Setup Assistant Complete");
    return true;  // success!
}

void MCPGenerator::generateCollisionTable(bool include_default, bool include_always,
                                               uint32_t trials, double min_collision_fraction,
                                               bool verbose) {
    default_collisions_.startGenerationThread(trials, min_collision_fraction, verbose);
    int thread_progress;
    int last_progress = 0;
    while ((thread_progress = default_collisions_.getThreadProgress()) < 100) {
        if (thread_progress - last_progress > 10) {
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
            last_progress = thread_progress;
        }
    }
    default_collisions_.joinGenerationThread();
    RCLCPP_INFO(LOGGER, "Collision table generated successfully");

    size_t skip_mask = 0;
    if (!include_default) skip_mask |= (1 << moveit_setup::srdf_setup::DEFAULT);
    if (!include_always) skip_mask |= (1 << moveit_setup::srdf_setup::ALWAYS);

    default_collisions_.linkPairsToSRDFSorted(skip_mask);
}

bool MCPGenerator::addVirtualJoints(std::string& child_link_name) {
    srdf::Model::VirtualJoint* virtual_joint = virtual_joints_.get("vjoint");

    // TODO: need to verify if that child_link exists in the group?
    auto link = urdf_config_->getModelPtr()->getLink(child_link_name);
    if (!link) {
        RCLCPP_ERROR(LOGGER, "Child link specified for the virtual joint is not part of URDF");
        return false;
    }

    virtual_joint->parent_frame_ = "virtual_link";
    virtual_joint->child_link_ = child_link_name;
    virtual_joint->type_ = "fixed";
    srdf_config_->updateRobotModel(moveit_setup::InformationFields::VIRTUAL_JOINTS);

    return true;
}

bool MCPGenerator::addPlanningGroup(const std::string& group_name, const std::string& base,
                                         const std::string& tip) {
    moveit_setup::srdf_setup::GroupMetaData meta_data;
    // set default values
    meta_data.kinematics_solver_ = "kdl_kinematics_plugin/KDLKinematicsPlugin";
    meta_data.kinematics_parameters_file_ = "";
    meta_data.default_planner_ = "";

    planning_groups_.get(group_name);
    planning_groups_.setMetaData(group_name, meta_data);
    try {
        planning_groups_.setChain(group_name, base, tip);
    } catch (const std::exception& e) {
        RCLCPP_ERROR(LOGGER, e.what());
        return false;
    }

    return true;
}

bool MCPGenerator::addDefaultControllers() {
    urdf_modifications_.refresh();
    auto default_interfaces = urdf_modifications_.getDefaultControlInterfaces();
    urdf_modifications_.setInterfaces(default_interfaces.command_interfaces,
                                      default_interfaces.state_interfaces);

    if (!moveit_controllers_->addDefaultControllers()) {
        RCLCPP_ERROR(LOGGER, "Error adding controllers: No Planning Groups configured!");
        return false;
    }
    if (!ros2_controllers_->addDefaultControllers()) {
        RCLCPP_ERROR(LOGGER, "Error adding controllers: No Planning Groups configured!");
        return false;
    }

    return true;
}

// ******************************************************************************************
// Save package using default path
// ******************************************************************************************
bool MCPGenerator::generatePackage(std::filesystem::path output_path) {
    config_files_.setPackagePath(output_path);
    config_files_.setPackageName(output_path.filename().string());
    config_files_.loadFiles();

    // Get path name
    std::string package_path_s = output_path.u8string();
    // Trim whitespace from user input
    boost::trim(package_path_s);

    // Check that a valid stack package name has been given
    if (package_path_s.empty()) {
        RCLCPP_WARN(
            LOGGER,
            "Error Generating: No package path provided. Please choose a directory location to "
            "generate the MoveIt configuration files.");
        return false;
    }

    config_files_.setGenerationTime();

    // Begin to create files and folders
    // ----------------------------------------------------------------------
    std::filesystem::path absolute_path;

    for (auto& gen_file : config_files_.getGeneratedFiles()) {
        absolute_path = gen_file->getPath();

        // Create the absolute path
        RCLCPP_DEBUG_STREAM(LOGGER, "Creating file " << absolute_path.string());

        // Run the generate function
        if (!gen_file->write()) {
            // Error occurred
            RCLCPP_ERROR_STREAM(LOGGER, "Error Generating File: Failed to generate folder or file: "
                                            << gen_file->getRelativePath() << " at location:\n"
                                            << absolute_path.c_str());
            return false;
        }
    }

    return true;
}

bool MCPGenerator::setAuthorInfo() {
    author_info_.setAuthorName("TODO");
    author_info_.setAuthorEmail("todo@todo.com");

    return true;
}