#!/usr/bin/env python

import rospy
from smach import State, StateMachine


def main():
    rospy.init_node('smach_usecase_executive')

    sm_root = StateMachine(outcomes=[])

    with sm_root:
        pass

    outcome = sm_root.execute()

    rospy.spin()


if __name__ == '__main__':
    main()
