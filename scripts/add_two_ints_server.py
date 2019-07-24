#!/usr/bin/env python

# import the python_course service
from python_course.srv import *
import rospy 

def request(req):
    my_classe = MyServiceResponse()
    
    my_classe.sys_active = True;
    my_classe.sys_voltage = 220;
    my_classe.sys_current = 2;
    my_classe.sys_temperature = 80;
    return my_classe

def server():
    rospy.init_node('server')
    rospy.Service('request', MyService, request)

    rospy.spin()

if __name__ == "__main__":
    server()