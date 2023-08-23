#include <moveit_setup_app_plugins/launches.hpp>
#include <moveit_setup_app_plugins/launches_config.hpp>
#include <moveit_setup_core_plugins/author_information.hpp>
#include <moveit_setup_core_plugins/configuration_files.hpp>
#include <moveit_setup_controllers/moveit_controllers.hpp>
#include <moveit_setup_controllers/ros2_controllers.hpp>
#include <moveit_setup_controllers/urdf_modifications.hpp>
#include <moveit_setup_framework/data/package_settings_config.hpp>
#include <moveit_setup_framework/data/srdf_config.hpp>
#include <moveit_setup_framework/data/urdf_config.hpp>
#include <moveit_setup_framework/data_warehouse.hpp>
#include <moveit_setup_srdf_plugins/default_collisions.hpp>
#include <moveit_setup_srdf_plugins/planning_groups.hpp>
#include <moveit_setup_srdf_plugins/virtual_joints.hpp>

#include <rclcpp/rclcpp.hpp>

class MCPGenerator {
   public:
    MCPGenerator(rclcpp::Node::SharedPtr node);

    bool loadNewFiles(const std::filesystem::path& urdf_file_path,
                      std::vector<std::string>& xacro_args);
    void generateCollisionTable(bool include_default, bool include_always, uint32_t trials,
                                double min_collision_fraction, bool verbose);
    bool addVirtualJoints(std::string& child_link_name);

    bool addPlanningGroup(const std::string& group_name, const std::string& base,
                          const std::string& tip);

    bool addDefaultControllers();

    bool generatePackage(std::filesystem::path output_path);

    bool setAuthorInfo();

    void writeSRDF(std::filesystem::path output_path) { srdf_config_->write(output_path); }

   private:
    std::shared_ptr<moveit_setup::PackageSettingsConfig> package_settings_;
    std::shared_ptr<moveit_setup::SRDFConfig> srdf_config_;
    std::shared_ptr<moveit_setup::URDFConfig> urdf_config_;
    std::shared_ptr<moveit_setup::app::LaunchesConfig> launches_config_;

    moveit_setup::DataWarehousePtr config_data_;
    moveit_setup::srdf_setup::DefaultCollisions default_collisions_;
    moveit_setup::srdf_setup::VirtualJoints virtual_joints_;
    moveit_setup::srdf_setup::PlanningGroups planning_groups_;
    std::shared_ptr<moveit_setup::controllers::Controllers> moveit_controllers_;
    std::shared_ptr<moveit_setup::controllers::Controllers> ros2_controllers_;
    moveit_setup::controllers::UrdfModifications urdf_modifications_;
    moveit_setup::core::ConfigurationFiles config_files_;
    moveit_setup::core::AuthorInformation author_info_;
    moveit_setup::app::Launches launch_files_;

    void loadURDFFile(const std::filesystem::path& urdf_file_path,
                      std::vector<std::string>& xacro_args);
};