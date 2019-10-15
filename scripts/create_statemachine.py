#!/usr/bin/env python
import os
import rospy
from smach import State, StateMachine
from smach_ros import IntrospectionServer
from test_state import *
from state_machine.msg import StateMachine_msgs

flag = True
statemachine = StateMachine(outcomes=['success', 'failed'])

def tuples_to_dict(keys, values):
    transition = {}
    for key, value in zip(keys, values):
        transition[key] = value
    return transition

def callback(message):
    global flag
    global statemachine
    if flag:
        kwargs = {}
        if message.keywords:
            kwargs = tuples_to_dict(message.keywords, message.args)
        with statemachine:
            StateMachine.add(message.id, globals()[message.statename](**kwargs), \
            transitions=tuples_to_dict(message.src, message.dst))
        if message.is_end is True:
            flag = False
            while True:
                status = statemachine.execute()
                if status == 'success':
                    print('===SUCCESS!===')
                    print('===RESTART STATE MACHINE===')
                else:
                    print('###FAILED...###')
                    os._exit(1)

if __name__ == '__main__':
    rospy.init_node('create_statemachine')
    sub = rospy.Subscriber('state', StateMachine_msgs, callback)
    sis = IntrospectionServer('server_name', statemachine, '/SM_ROOT')
    sis.start()
    rospy.spin()

