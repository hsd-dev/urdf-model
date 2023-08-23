cmake_minimum_required(VERSION 3.10.2)
project(kinematics_model_generator)

# Common cmake code applied to all moveit packages
find_package(moveit_common REQUIRED)
moveit_package()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(urdf REQUIRED)

install(DIRECTORY resources DESTINATION share/${PROJECT_NAME})

# Install Python modules
ament_python_install_package(${PROJECT_NAME})
# Install Python executables
install(PROGRAMS
  scripts/batch_model_generator.py
  scripts/urdf_parser.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
