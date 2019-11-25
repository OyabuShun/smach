#!/usr/bin/env python

import rospy
from smach import State, StateMachine
from smach_ros import IntrospectionServer, ServiceState
from std_srvs.srv import Empty, EmptyRequest
from turtlesim.srv import Spawn, SpawnRequest


def main():
    rospy.init_node('smach_usecase_executive')

    sm_root = StateMachine(outcomes=['preempted', 'aborted', 'succeeded'])

    with sm_root:
        StateMachine.add(
            'RESET',
            ServiceState(
                'service_name',
                Empty,
                request=EmptyRequest),
            transitions={
                'succeeded': 'SPAWN'})
        StateMachine.add(
            'SPAWN',
            ServiceState(
                'service_name',
                Spawn,
                request=SpawnRequest),
            transitions={
                'preemtped': 'preemtped',
                'aborted': 'aborted',
                'succeeded': 'succeeded'})

    sis = IntrospectionServer('exmaple', sm_root, '/USE_CASE')

    outcome = sm_root.execute()

    rospy.spin()


if __name__ == '__main__':
    main()
