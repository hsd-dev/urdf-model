cmake_minimum_required(VERSION 3.10.2)
project(kinematics_model_generator)

# Common cmake code applied to all moveit packages
find_package(moveit_common REQUIRED)
moveit_package()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(moveit_core REQUIRED)
find_package(moveit_ros_planning REQUIRED)
find_package(moveit_ros_visualization REQUIRED)
find_package(moveit_setup_app_plugins REQUIRED)
find_package(moveit_setup_core_plugins REQUIRED)
find_package(moveit_setup_controllers REQUIRED)
find_package(moveit_setup_framework REQUIRED)
find_package(moveit_setup_srdf_plugins REQUIRED)
find_package(ompl REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(srdfdom REQUIRED)
find_package(urdf REQUIRED)

set(THIS_PACKAGE_INCLUDE_DEPENDS
  moveit_core
  moveit_ros_planning
  moveit_ros_visualization
  moveit_setup_app_plugins
  moveit_setup_core_plugins
  moveit_setup_controllers
  moveit_setup_framework
  moveit_setup_srdf_plugins
  rclcpp
  urdf
  srdfdom
)

add_executable(mcp_generator
  src/main.cpp
  src/mcp_generator.cpp
)
target_include_directories(mcp_generator PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_link_libraries(
  mcp_generator
)

ament_target_dependencies(
  mcp_generator
  ${THIS_PACKAGE_INCLUDE_DEPENDS}
)

install(
  TARGETS
    mcp_generator
  EXPORT ${PROJECT_NAME}Targets
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION lib/${PROJECT_NAME}
  INCLUDES DESTINATION include
)
install(DIRECTORY resources DESTINATION share/${PROJECT_NAME})
ament_export_targets(${PROJECT_NAME}Targets HAS_LIBRARY_TARGET)
ament_export_dependencies(${THIS_PACKAGE_INCLUDE_DEPENDS})

# Install Python modules
ament_python_install_package(${PROJECT_NAME})
# Install Python executables
install(PROGRAMS
  scripts/batch_model_generator.py
  scripts/urdf_parser.py
  scripts/update_mcp.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
