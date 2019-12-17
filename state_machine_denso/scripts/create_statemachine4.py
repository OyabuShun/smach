#!/usr/bin/env python

import os
import rospy
from smach import State, StateMachine
from smach_ros import IntrospectionServer
from geometry_msgs.msg import PoseStamped
from denso_state_smach import *
#from test_state import *
#from state_machine_denso.msg import StateMachine_msgs2
from denso_state_msgs.msg import StateMachine_msgs2

flag = True
sm_top = StateMachine(outcomes=['success', 'failed'])
sm_sub = StateMachine(outcomes=['success', 'failed'])
sm_sub2 = StateMachine(outcomes=['success', 'failed'])
#sm_sub3 = StateMachine(outcomes=['success', 'failed'])


def tuples_to_dict(keys, values):
    transition = {}
    for key, value in zip(keys, values):
        transition[key] = value
    return transition


def callback(message):
    global flag
    global sm_top
    global sm_sub
    global sm_sub2
    if flag:
        kwargs = PoseStamped()
        kwargs.pose = message.workpoint
        grasp_object_pose = PoseStamped()
        grasp_object_pose.pose.position.x = 0.5
        grasp_object_pose.pose.position.y = -0.3
        grasp_object_pose.pose.position.z = 0.3
        grasp_object_pose.pose.orientation.x = 1.0

        count = 0

        """
        #---success way---
#        if message.id == 'InitialState':
        with sm_top:
            StateMachine.add(
                "InitialState",
                InitialState(grasp_object_pose),
                transitions={
                    'success': 'SUB',
                    'failed': 'failed'})
        if message.id == 'BeforeAssemble':
            with sm_top:
               # sm_sub = StateMachine(outcomes=['success', 'failed'])
                with sm_sub:
                    StateMachine.add(
                        "BeforeGrasp",
                        BeforeGrasp(grasp_object_pose),
                        transitions={
                            'success': 'AfterGrasp',
                            'failed': 'failed'})
                    StateMachine.add(
                        "AfterGrasp",
                        AfterGrasp(grasp_object_pose),
                        transitions={
                            'success': 'BeforeAssemble',
                            'failed': 'failed'})


                    print(message.id)
                    StateMachine.add(
                        message.id,
                        globals()[
                            message.statename](kwargs),
                        transitions=tuples_to_dict(
                            message.src,
                            message.dst))
                StateMachine.add("SUB", sm_sub, transitions={'success': 'success', 'failed': 'failed'})
        """
        count = 0
        if message.id == 'InitialState':
            with sm_top:
                print(message.id)
                StateMachine.add(
                    message.id,
                    globals()[
                        message.statename](kwargs),
                    transitions=tuples_to_dict(
                        message.src,
                        message.dst))

                StateMachine.add(
                    'SUB', sm_sub, transitions={
                        'success': 'SUB2', 'failed': 'failed'})
                StateMachine.add(
                    'SUB2', sm_sub2, transitions={
                        'success': 'success', 'failed': 'failed'})
#                StateMachine.add('SUB3', sm_sub3, transitions={'success': 'success', 'failed': 'failed'})
        elif message.id != 'FinalState':
            for j in range(5):
                for k in range(3):
                    if message.id != 'AfterAssembleRepetition' and j == 0 and k == 0:
                        with sm_top:
                            print(message.id)
                            print(kwargs)
                            with sm_sub:
                                StateMachine.add(
                                    message.id,
                                    globals()[
                                        message.statename](kwargs),
                                    transitions=tuples_to_dict(
                                        message.src,
                                        message.dst))
                        break
                    elif message.id == 'AfterAssembleRepetition' and j == 0 and k == 0:
                        with sm_top:
                            print(message.id)
                            print(kwargs)
                            with sm_sub:
                                StateMachine.add(
                                    message.id,
                                    globals()[
                                        message.statename](kwargs),
                                    transitions=tuples_to_dict(
                                        message.src,
                                        message.dst))
                        k += 1
                        break

                """
                if message.id == 'AfterAssembleRepetition' and count == 0:
                    with sm_top:
                        print(message.id)
                        print(kwargs)
                        with sm_sub:
                            StateMachine.add(
                                message.id,
                                globals()[
                                    message.statename](kwargs),
                                transitions=tuples_to_dict(
                                    message.src,
                                    message.dst))

                #count += 1
                if message.id != 'AfterAssembleRepetition' and count2 == 1:
                    with sm_top:
                        print(message.id)
                        print(kwargs)
                        with sm_sub2:
                            StateMachine.add(
                                message.id,
                                globals()[
                                    message.statename](kwargs),
                                transitions=tuples_to_dict(
                                    message.src,
                                    message.dst))
                    break
                elif message.id == 'AfterAssembleRepetition' and count2 == 1:
                    with sm_top:
                        print(message.id)
                        print(kwargs)
                        with sm_sub2:
                            StateMachine.add(
                                message.id,
                                globals()[
                                    message.statename](kwargs),
                                transitions=tuples_to_dict(
                                    message.src,
                                    message.dst))
                    break
                """
                if message.id == 'AfterAssemble':
                    with sm_top:
                        print(message.id)
                        print(kwargs)
                        with sm_sub2:
                            StateMachine.add(
                                message.id,
                                globals()[
                                    message.statename](kwargs),
                                transitions=tuples_to_dict(
                                    message.src,
                                    message.dst))
                    break

                #count += 1
                # print(count)

        else:
            with sm_top:
                print(message.id)
                StateMachine.add(
                    message.id,
                    globals()[
                        message.statename](kwargs),
                    transitions=tuples_to_dict(
                        message.src,
                        message.dst))

                #StateMachine.add('SUB', sm_sub, transitions={'success': 'FinalState', 'failed': 'failed'})
        # if message.id == 'FinalState':
         #   with sm_top:
          #      StateMachine.add('SUB', sm_sub, transitions={'success': 'success', 'failed': 'failed'})

        """
        if message.id == 'InitialState':
            print(message.id)
            with sm_top:
                StateMachine.add(
                    message.id,
                    globals()[
                        message.statename](kwargs),
                    transitions=tuples_to_dict(
                        message.src,
                        message.dst))


                print(message.id)
        else:
            with sm_top:
                sm_sub = StateMachine(outcomes=['success', 'failed'])

                with sm_sub:
                    StateMachine.add(
                        message.id,
                        globals()[
                            message.statename](kwargs),
                        transitions=tuples_to_dict(
                            message.src,
                            message.dst))
                StateMachine.add('SUB', sm_sub, transitions={'success': 'success', 'failed': 'failed'})
        """
        if message.is_end is True:
            # with sm_top:

             #   sm_sub = StateMachine(outcomes=['success', 'failed'])
             #   StateMachine.add('SUB', sm_sub, transitions={'success': 'success', 'failed': 'failed'})

            flag = False
            while True:
                sis = IntrospectionServer('server_name', sm_top, '/SM_ROOT')
                sis.start()
                #sis = IntrospectionServer('server_name1', sm_sub, '/SUB')
                # sis.start()
                status = sm_top.execute()
                if status == 'success':
                    print('===SUCCESS!===')
                    print('===RESTART STATE MACHINE===')
                    os._exit(1)
                else:
                    print('###FAILED...###')
                    os._exit(1)


if __name__ == '__main__':
    rospy.init_node('create_statemachine')
    sub = rospy.Subscriber('/state_data', StateMachine_msgs2, callback)
    sis = IntrospectionServer('server_name', sm_top, '/SM_ROOT')
    sis.start()
    sis = IntrospectionServer('server_name', sm_sub, '/SUB')
    sis.start()
    rospy.spin()
