#!/usr/bin/env python

import rospy
from state_machine_denso.msg import StateMachine_msgs2
from state_machine_denso.srv import WorkPointSrv
from time import sleep


class Publisher(object):
    def __init__(self):
        rospy.wait_for_service('/state_data_service')
        self.state_data_service = rospy.ServiceProxy('/state_data_service', WorkPointSrv)
        self.state_data = rospy.Publisher('/state_data', StateMachine_msgs2, queue_size=1)

    def publisher_state_data(self):
        response = self.state_data_service()
        state_data_pub = StateMachine_msgs2()

        state_data_pub.src = ['success', 'failed']

        for i, name in enumerate(response.state):
            if response.state[i] == '100':
#                response.state[i] = 'InitialState'
                state_data_pub.statename = 'InitialState'
                state_data_pub.id = 'InitialState'
                state_data_pub.dst = ['BeforeGrasp', 'failed']
                state_data_pub.is_end = False
                sleep(5)
                self.state_data.publish(state_data_pub)
            elif response.state[i] == '200':
#                response.state[i] = 'BeforeGrasp'
                state_data_pub.statename = 'BeforeGrasp'
                state_data_pub.id = 'BeforeGrasp'
                state_data_pub.dst = ['AfterGrasp', 'failed']
                state_data_pub.is_end = False
                sleep(5)
                self.state_data.publish(state_data_pub)
            elif response.state[i] == '300':
#                response.state[i] = 'AfterGrasp'
                state_data_pub.statename = 'AfterGrasp'
                state_data_pub.id = 'AfterGrasp'
                state_data_pub.dst = ['success', 'failed']
                state_data_pub.keywords = ['sleeptime']
                state_data_pub.args = ['3']
                state_data_pub.is_end = True
                sleep(5)
                self.state_data.publish(state_data_pub)

        print('published')

if __name__ == '__main__':
    rospy.init_node("state_data")
    publish = Publisher()
    publish.publisher_state_data()
    rospy.spin()
