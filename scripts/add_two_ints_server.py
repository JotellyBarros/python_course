#!/usr/bin/env python

# import the python_course service
from python_course.srv import *
import rospy 

def add_two_ints(req):
    print("Returning [%s + %s = %s]" % (req.a, req.b, (req.a + req.b)))
    return MyServiceResponse(req.a + req.b)

def add_two_ints_server():
    print("Start Server:")
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', MyService, add_two_ints)

    # spin() keeps Python from exiting until node is shutdown
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()