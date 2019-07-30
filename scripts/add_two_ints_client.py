#!/usr/bin/env python

import sys
import rospy

# import the python_course service
from std_srvs.srv import SetBool
from python_course.srv import *

# def SetBool():
#     rospy.wait_for_service('enable_output')
#     enable_output = rospy.ServiceProxy('enable_output', SetBool)
#     resp1 = enable_output(True)
#     return resp1

def setvoltage():
    rospy.wait_for_service('set_voltage')

    set_voltage = rospy.ServiceProxy('set_voltage', SetFloat64)
    resp1 = set_voltage(10)
    return resp1

def setcurrent():
    rospy.wait_for_service('set_current')
    set_current = rospy.ServiceProxy('set_current', SetFloat64)
    resp1 = set_current(100)
    return resp1

if __name__ == "__main__":
    # print("{return_server}".format(return_server=SetBool()))
    print("{return_server}".format(return_server=setvoltage()))
    print("{return_server}".format(return_server=setcurrent()))