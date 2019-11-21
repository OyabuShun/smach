#!/usr/bin/env python

import rospy
from smach import State, StateMachine
from smach_ros import IntrospectionServer, ServiceState
from smach_usecase_srv.srv import Reset, ResetRequest


def main():
    rospy.init_node('smach_usecase_executive')

    sm_root = StateMachine(outcomes=['preempted', 'aborted', 'succeeded'])

    with sm_root:
        StateMachine.add(
            'RESET',
            ServiceState(
                'service_name',
                Reset,
                request=ResetRequest),
            transitions={
                'succeeded': 'SPAWN'})
        StateMachine.add(
            'SPAWN',
            ServiceState(
                'service_name',
                turtlesim.srv,
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
