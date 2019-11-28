#!/usr/bin/env python

import os
import rospy
from smach import State, StateMachine
from smach_ros import IntrospectionServer
from test_state import *
from state_machine_denso.msg import StateMachine_msgs

flag = True
sm = StateMachine(outcomes=['success', 'failed'])


def tuples_to_dict(keys, values):
    transition = {}
    for key, value in zip(keys, values):
        transition[key] = value
    return transition


def callback(message):
    global flag
    global sm
    if flag:
        kwargs = {}
        if message.keywords:
            kwargs = tuples_to_dict(message.keywords, message.args)
            print(kwargs)


if __name__ == '__main__':
    rospy.init_node('create_statemachine')
    sub = rospy.Subscriber('state', StateMachine_msgs, callback)
    sis = IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()
    rospy.spin()
