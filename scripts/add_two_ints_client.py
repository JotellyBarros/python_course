#!/usr/bin/env python

import sys
import rospy

# import the python_course service
from python_course.srv import *

def client(parameter_value):
    rospy.wait_for_service('request')
    try:
        request = rospy.ServiceProxy('request', MyService)
        resp1 = request()
        if (parameter_value == "voltage"):
            return resp1.sys_voltage
        elif (parameter_value == "current"):
            return resp1.sys_current
        elif (parameter_value == "temperature"):
            return resp1.sys_temperature
        elif (parameter_value == "active"):
            return resp1.sys_active
        else:
            return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s" %e

def usage():
    return "%s [parameter]" %sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        parameter = (sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print("{parameter} : {return_server}".format(parameter = parameter, return_server=client(parameter)))