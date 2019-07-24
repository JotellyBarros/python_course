#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import rospy
from std_msgs.msg import String

print ("Python version:", (sys.version), '\n')

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # True ensures that your node has a unique name by adding random numbers to the end of NAME
    rospy.init_node('talker', anonymous=True)

    # Loop 10 times per second
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
