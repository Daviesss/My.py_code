#!/usr/bin/env python
import rospy 
from geometry_msgs.msg import Twist 

command_vel = '/cmd_vel'



def move_foward(speed):
    rospy.init_node('move',anonymous=True)
    pub = rospy.Publisher(command_vel,Twist,queue_size=1)
    velocity_message = Twist ()

    velocity_message.linear.x = speed 
    loop = rospy.Rate(10)


    while not rospy.is_shutdown():
        rospy.loginfo("The robot moves foward")
        pub.publish(velocity_message)


if __name__ == '__main__':
    try :
        move_foward(1.0)

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")





