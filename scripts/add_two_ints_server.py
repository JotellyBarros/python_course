#!/usr/bin/env python
# import the python_course service
import rospy

from std_srvs.srv import SetBool
from python_course.srv import *
from python_course.msg import *
# from std_msgs.msg import Float64
from power_supply import *  # Class Power Supple


# Changes the power supply of the source
def callback_output(req):
    return supply.set_enable_output(req.data)

# Changes the mode supply voltage
def callback_voltage(req):
    return supply.set_voltage_set_point(req.data)

# Changes the mode supply current
def callback_current(req):
    return supply.set_current_set_point(req.data)


def server_supply():
    rospy.init_node('server_supply', anonymous=True)

    rospy.Service('enable_output', SetBool, callback_output)
    rospy.Service('set_voltage', SetFloat64, callback_voltage)
    rospy.Service('set_current', SetFloat64, callback_current)

    rate = rospy.Rate(1)
    # create name publisher with default queue size and rate
    pub = rospy.Publisher('state', PowerSupplyState, queue_size=10)

    while not rospy.is_shutdown():
        new_msg = PowerSupplyState()

        # new_msg.op_mode = new_msg.VOLTAGE_MODE

        new_msg.enable_output = supply.enable_output
        new_msg.op_mode = supply.op_mode
        new_msg.voltage_set_point = supply.voltage_set_point
        new_msg.voltage = supply.voltage
        new_msg.current_set_point = supply.current_set_point
        new_msg.current = supply.current

        rospy.loginfo("\nMessages from Server:\n{}".format(new_msg))
        # pub.publish(new_msg)
        rate.sleep()

    rospy.spin()


if __name__ == "__main__":
    supply = SupplyParameters()
    # supply.printStatus()
    server_supply()
