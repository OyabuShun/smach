#!/usr/bin/env python

import rospy
from smach import State, StateMachine
from smach_ros import IntrospectionServer, ServiceState
from std_srvs.srv import Empty, EmptyRequest
from turtlesim.srv import Spawn, SpawnRequest
from time import sleep

class Reset(State):
    def __init__(self):
        State.__init__(self, outcomes=['succeeded'])

    def execute(self, userdata):
        sleep(1)
        rospy.loginfo('Executing State Reset')
        return 'succeeded'

class Spawn(State):
    def __init__(self):
        State.__init__(self, outcomes=['preemtped', aborted, 'succeeded'])

    def execute(self, userdata):
        sleep(1)
        print('Execuing State Spawn')
        return 'aborted'


def main():
    rospy.init_node('smach_usecase_executive')

    sm_root = StateMachine(outcomes=['preempted', 'aborted', 'succeeded'])

    with sm_root:
        StateMachine.add(
            'RESET',
            ServiceState(
                '/reset',
                Empty,
                request=EmptyRequest()),
            transitions={
                'succeeded': 'SPAWN'})
        StateMachine.add(
            'SPAWN',
            ServiceState(
                '/spawn',
                Empty,
                request=EmptyRequest()),
                #request=SpawnRequest(1.0, 1.0, 2.0, 'kkk')),
                transitions={'aborted': 'aborted'})
#            transitions={
#                'preemtped': 'preemtped',
#                'aborted': 'aborted',
#                'succeeded': 'succeeded'})

    sis = IntrospectionServer('exmaple', sm_root, '/USE_CASE')
    sis.start()

    outcome = sm_root.execute()

    rospy.spin()


if __name__ == '__main__':
    main()
