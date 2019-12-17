#!/usr/bin/env python

import rospy
#from state_machine_denso.msg import StateMachine_msgs2
from denso_state_msgs.msg import StateMachine_msgs2
#from state_machine_denso.srv import WorkPointSrv
from denso_state_srvs.srv import WorkPointSrv
from denso_state_srvs.srv import WorkPointServiceProvider
from time import sleep


class Publisher(object):
    def __init__(self):
        rospy.wait_for_service('/state_data_service')
        # rospy.wait_for_service('/test')
        self.state_data_service = rospy.ServiceProxy(
            '/state_data_service', WorkPointSrv)
        #self.state_data_service = rospy.ServiceProxy('/test', WorkPointServiceProvider)
        self.state_data = rospy.Publisher(
            '/state_data', StateMachine_msgs2, queue_size=10)

    def publisher_state_data(self):
        response = self.state_data_service()
        state_data_pub = StateMachine_msgs2()

        print(response)

        state_data_pub.src = ['success', 'failed']
        state_data_pub.is_end = False
        print(state_data_pub.src)
        print(response.grasp)
        print(response.assemble)
        for i, name in enumerate(response.state):

            if response.state[i] == '100':
                #                response.state[i] = 'InitialState'
                state_data_pub.statename = 'InitialState'
                state_data_pub.id = 'InitialState'
                state_data_pub.dst = ['SUB', 'failed']
                #state_data_pub.dst = ['BeforeGrasp', 'failed']
                state_data_pub.workpoint = response.grasp
                sleep(3)
                self.state_data.publish(state_data_pub)

            elif response.state[i] == '200':
                #                response.state[i] = 'BeforeGrasp'
                state_data_pub.statename = 'BeforeGrasp'
                state_data_pub.id = 'BeforeGrasp'
                state_data_pub.dst = ['AfterGrasp', 'failed']
                sleep(3)
                self.state_data.publish(state_data_pub)

            elif response.state[i] == '300':
                #                response.state[i] = 'AfterGrasp'
                state_data_pub.statename = 'AfterGrasp'
                state_data_pub.id = 'AfterGrasp'
                state_data_pub.dst = ['BeforeAssemble', 'failed']
                state_data_pub.workpoint = response.assemble
                sleep(3)
                self.state_data.publish(state_data_pub)

            elif response.state[i] == '400':
                state_data_pub.statename = 'BeforeAssemble'
                state_data_pub.id = 'BeforeAssemble'
                state_data_pub.dst = ['AfterAssemble', 'failed']
                state_data_pub.workpoint = response.assemble
                sleep(3)
                self.state_data.publish(state_data_pub)

            elif response.state[i] == '500':
                state_data_pub.statename = 'AfterAssemble'
                state_data_pub.id = 'AfterAssemble'
                state_data_pub.dst = ['FinalState', 'failed']
                sleep(3)
                self.state_data.publish(state_data_pub)
            elif response.state[i] == '600':
                state_data_pub.statename = 'FinalState'
                state_data_pub.id = 'FinalState'
                state_data_pub.dst = ['success', 'failed']
                state_data_pub.is_end = True
                sleep(3)
                self.state_data.publish(state_data_pub)

            """
            elif response.state[i] == '700':
                state_data_pub.statename = 'InitialState'
                state_data_pub.id = 'InitialState2'
                state_data_pub.dst = ['success', 'failed']
                state_data_pub.is_end = True
                state_data_pub.workpoint = response.grasp
                sleep(3)
                self.state_data.publish(state_data_pub)
            """

        print('published')
        print(state_data_pub)


if __name__ == '__main__':
    rospy.init_node("state_data")
    publish = Publisher()
    publish.publisher_state_data()
    rospy.spin()
