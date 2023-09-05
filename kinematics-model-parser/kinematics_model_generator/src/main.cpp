#include <boost/program_options.hpp>
#include <fstream>  // for reading in urdf

#include "kinematics_model_generator/mcp_generator.hpp"

namespace po = boost::program_options;

static const rclcpp::Logger LOGGER = rclcpp::get_logger("mcp_generator");

int main(int argc, char* argv[])
{
  std::filesystem::path urdf_path;
  std::filesystem::path output_path;

  std::vector<std::string> group_name, base_link, end_link;
  std::string virtual_child_link;

  bool include_default = false, include_always = false, keep_old = false, verbose = false;

  double min_collision_fraction = 1.0;

  uint32_t never_trials = 0;

  po::options_description desc("Allowed options");
  desc.add_options()("help", "show help")("urdf", po::value(&urdf_path), "path to URDF ( or xacro)")(
      "group_name", po::value(&group_name)->multitoken(),
      "Move group name")("base_link", po::value(&base_link)->multitoken(),
                         "Base link name")("end_link", po::value(&end_link)->multitoken(), "End link name")(
      "virtual_child_link", po::value(&virtual_child_link), "End link name")("output", po::value(&output_path),
                                                                             "output path for SRDF")(
      "xacro-args", po::value<std::vector<std::string>>()->composing(), "additional arguments for xacro")(
      "default", po::bool_switch(&include_default), "disable default colliding pairs")(
      "always", po::bool_switch(&include_always), "disable always colliding pairs")("keep", po::bool_switch(&keep_old),
                                                                                    "keep disabled link from SRDF")(
      "verbose", po::bool_switch(&verbose), "verbose output")("trials", po::value(&never_trials),
                                                              "number of trials for searching never colliding pairs")(
      "min-collision-fraction", po::value(&min_collision_fraction),
      "fraction of small sample size to determine links that are always colliding");

  po::positional_options_description pos_desc;
  pos_desc.add("xacro-args", -1);

  po::variables_map vm;
  po::store(po::command_line_parser(argc, argv).options(desc).positional(pos_desc).run(), vm);
  po::notify(vm);

  if (vm.count("help"))
  {
    std::cout << desc << '\n';
    return 1;
  }

  rclcpp::init(argc, argv);
  rclcpp::Node::SharedPtr node = std::make_shared<rclcpp::Node>("mcp_generator");

  if (urdf_path.empty())
  {
    RCLCPP_ERROR_STREAM(LOGGER, "Please provide URDF path");
    return 1;
  }

  std::vector<std::string> xacro_args;
  if (vm.count("xacro-args"))
  {
    xacro_args = vm["xacro-args"].as<std::vector<std::string>>();
  }

  if ((group_name.size() != base_link.size()) || (group_name.size() != end_link.size()))
  {
    RCLCPP_ERROR_STREAM(LOGGER, "Incorrect planning groups.");
    return 1;
  }

  MCPGenerator mcp_generator(node);
  mcp_generator.loadNewFiles(urdf_path, xacro_args);

  RCLCPP_INFO_STREAM(LOGGER, "Completed loading files.");

  // 1. generate self-collision matrix
  mcp_generator.generateCollisionTable(include_default, include_always, never_trials, min_collision_fraction, verbose);

  // 2. add virtual joints - normally an optional step
  // TODO: child_link should ideally be the root of the robot model
  // - use xacro parser to retrieve that
  bool success = mcp_generator.addVirtualJoints(virtual_child_link);

  if (!success)
  {
    return -1;
  }

  // 3. add planning group(s)
  // TODO: this would be in a for-loop for a machine
  // success = mcp_generator.addPlanningGroup("c_203_robot_arm", "c_203_robot_arm_base_link",
  //                                               "c_203_robot_arm_link_4");
  // success &= mcp_generator.addPlanningGroup("c_204_pick_place_system", "c_204_pick_place_system_base_link",
  //                                               "c_204_pick_place_system_link_2");
  // success &= mcp_generator.addPlanningGroup("c_206_height_check_system", "c_206_height_check_system_base_link",
  //                                               "c_206_height_check_system_link_2");
  // success &= mcp_generator.addPlanningGroup("c_207_workpiece_feeder", "c_207_workpiece_feeder_base_link",
  //                                               "c_207_workpiece_feeder_zone_link");
  // success &= mcp_generator.addPlanningGroup("c_208_workpiece_lifter", "c_208_workpiece_lifter_base_link",
  //                                               "c_208_workpiece_lifter_link_1");

  for (size_t i = 0; i < group_name.size(); i++)
  {
    success &= mcp_generator.addPlanningGroup(group_name[i], base_link[i], end_link[i]);
    std::cout << group_name[i] << " " << base_link[i] << " " << end_link[i] << std::endl;
  }

  if (!success)
  {
    return -1;
  }

  // // 4. add moveit and ros controllers; and setup ros2_control.xacro
  success = mcp_generator.addDefaultControllers();
  if (!success)
  {
    return -1;
  }

  // 5. generate package
  mcp_generator.generatePackage(output_path);

  // 6. set author info
  mcp_generator.setAuthorInfo();

  return 0;
}
