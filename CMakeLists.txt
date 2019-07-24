cmake_minimum_required(VERSION 2.8.3)
project(python_course)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  roslint
  message_generation
)

add_message_files(DIRECTORY msg FILES MyMonitor.msg)
add_service_files(DIRECTORY srv FILES MyService.srv)

# # Generate services in the 'srv' folder
# add_service_files(FILES
#   MyService.srv
# )

# # Generate messages in the 'msg' folder
# add_message_files(FILES
#   MyMonitor.msg
# )

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
  scripts/add_two_ints_client.py
  scripts/add_two_ints_server.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/scripts
)

## Install Python ##
# install(PROGRAMS
#   scripts/course_python.py
#   scripts/listener.py
#   scripts/add_two_ints_client.py
#   scripts/add_two_ints_server.py
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )