#!/usr/bin/env python

import rospy
from smach import StateMachine
from smach_ros import IntrospectionServer
from geometry_msgs.msg import PoseStamped
from denso_state_smach import *
from denso_state_srvs.srv import WorkPointServiceProvider


if __name__ == '__main__':
    rospy.init_node('state_machine_p_and_p_example')

    relative_grasp_pose = PoseStamped()
    relative_grasp_pose.pose.position.x = 0.5
    relative_grasp_pose.pose.position.y = -0.3
    relative_grasp_pose.pose.position.x = 0.3
    relative_grasp_pose.pose.orientation.x = 1.0
    relative_grasp_pose2 = PoseStamped()
    relative_grasp_pose2.pose.position.x = 0.5
    relative_grasp_pose2.pose.position.y = -0.4
    relative_grasp_pose2.pose.position.z = 0.3
    relative_grasp_pose2.pose.orientation.x = 1.0
    relative_assemble_pose = PoseStamped()
    relative_assemble_pose.pose.position.x = 0.5
    relative_assemble_pose.pose.position.y = 0.3
    relative_assemble_pose.pose.position.z = 0.3
    relative_assemble_pose.pose.orientation.x = 1.0
    relative_assemble_pose2 = PoseStamped()
    relative_assemble_pose2.pose.position.x = 0.5
    relative_assemble_pose2.pose.position.y = 0.4
    relative_assemble_pose2.pose.position.z = 0.3
    relative_assemble_pose2.pose.orientation.x = 1.0

    sm_top = StateMachine(outcomes=['success', 'failed'])
    with sm_top:
        StateMachine.add(
            "InitialState",
            InitialState(relative_grasp_pose),
            transitions={
                'success': 'SUB1',
                'failed': 'failed'})

        sm_sub1 = StateMachine(outcomes=['success', 'failed'])
        with sm_sub1:
            StateMachine.add(
                "BeforeGrasp",
                BeforeGrasp(),
                transitions={
                    'success': 'AfterGrasp',
                    'failed': 'failed'})
            StateMachine.add(
                "AfterGrasp",
                AfterGrasp(relative_assemble_pose),
                transitions={
                    'success': 'BeforeAssemble',
                    'failed': 'failed'})
            StateMachine.add(
                "BeforeAssemble",
                BeforeAssemble(relative_assemble_pose),
                transitions={
                    'success': 'AfterAssemble',
                    'failed': 'failed'})
            StateMachine.add(
                "AfterAssemble",
                AfterAssemble(),
                transitions={
                    'success': 'success',
                    'failed': 'failed'})
        StateMachine.add(
            "SUB1", sm_sub1, transitions={
                'success': 'FinalState', 'failed': 'failed'})


        StateMachine.add(
            "FinalState",
            FinalState(),
            transitions={
                'success': 'success', 'failed': 'failed'})

    sis = IntrospectionServer('p_and_p_example', sm_top, '/SM_ROOT')
    sis.start()

    sm_top.execute()
    rospy.spin()
