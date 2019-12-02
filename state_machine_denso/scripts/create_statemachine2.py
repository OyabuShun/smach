#!/usr/bin/env python

import os
import rospy
from smach import State, StateMachine
from smach_ros import IntrospectionServer
from test_state import *
from state_machine_denso.msg import StateMachine_msgs2

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
        with sm:
            StateMachine.add(
                message.id,
                globals()[
                    message.statename](**kwargs),
                transitions=tuples_to_dict(
                    message.src,
                    message.dst))
        if message.is_end is True:
            flag = False
            while True:
                status = sm.execute()
                if status == 'success':
                    print('===SUCCESS!===')
                    print('===RESTART STATE MACHINE===')
                else:
                    print('###FAILED...###')
                    os._exit(1)


if __name__ == '__main__':
    rospy.init_node('create_statemachine')
    sub = rospy.Subscriber('/state_data', StateMachine_msgs2, callback)
    sis = IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()
    rospy.spin()
