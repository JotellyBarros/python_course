cmake_minimum_required(VERSION 2.8.3)
project(python_course)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  roslint
  std_msgs
  message_generation
)

## Generate services in the 'srv' folder
add_service_files(FILES
  SetFloat64.srv
)

## Generate messages in the 'msg' folder
add_message_files(FILES
  PowerSupplyState.msg
)

# Actually generate the language-specific message and service files
## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs  # Or other packages containing msgs
)

## catkin specific configuration ##
catkin_package(CATKIN_DEPENDS
  message_runtime 
  std_msgs
)

## Build ##
include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/debug_power_supply.py
  scripts/add_two_ints_client.py
  scripts/add_two_ints_server.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/scripts
)
