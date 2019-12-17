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
        # rospy.wait_for_service('/state_data_service')
        rospy.wait_for_service('/test')
#        self.state_data_service = rospy.ServiceProxy('/state_data_service', WorkPointSrv)
        self.state_data_service = rospy.ServiceProxy(
            '/test', WorkPointServiceProvider)
        self.state_data = rospy.Publisher(
            '/state_data', StateMachine_msgs2, queue_size=10)

    def publisher_state_data(self):
        global k
        response = self.state_data_service()
        state_data_pub = StateMachine_msgs2()

        print(response)

        state_data_pub.src = ['success', 'failed']
        state_data_pub.is_end = False

        for j, name in enumerate(response.state):
            if response.state[j] == '600':
                response.state[j - 1] = '450'
                print(response.state)
        count = 0
        for i, name in enumerate(response.state):
            for k in range(2):
                if response.state[i] == '100':
                    state_data_pub.statename = 'InitialState'
                    state_data_pub.id = 'InitialState'
                    state_data_pub.dst = ['SUB', 'failed']
                    #state_data_pub.dst = ['BeforeGrasp', 'failed']
                    state_data_pub.workpoint = response.grasp[count]
                    print(count)
                    sleep(3)
                    print(state_data_pub.workpoint)
                    self.state_data.publish(state_data_pub)
                    break

                elif response.state[i] == '200':
                    state_data_pub.statename = 'BeforeGrasp'
                    state_data_pub.id = 'BeforeGrasp'
                    state_data_pub.dst = ['AfterGrasp', 'failed']
                    print('gg')
                    sleep(3)
                    self.state_data.publish(state_data_pub)
                    break

                elif response.state[i] == '300':
                    state_data_pub.statename = 'AfterGrasp'
                    state_data_pub.id = 'AfterGrasp'
                    state_data_pub.dst = ['BeforeAssemble', 'failed']
                    state_data_pub.workpoint = response.assemble[count]
                    sleep(3)
                    print(state_data_pub.workpoint)
                    self.state_data.publish(state_data_pub)
                    break

                elif response.state[i] == '400':
                    state_data_pub.statename = 'BeforeAssemble'
                    state_data_pub.id = 'BeforeAssemble'
                    state_data_pub.dst = ['AfterAssemble', 'failed']
                    state_data_pub.workpoint = response.assemble[count]
                    sleep(3)
                    count += 1
                    print(state_data_pub.workpoint)
                    self.state_data.publish(state_data_pub)
                    print(count)
                    break

                elif response.state[i] == '500':
                    state_data_pub.statename = 'AfterAssembleRepetition'
                    state_data_pub.id = 'AfterAssembleRepetition'
                    state_data_pub.dst = ['success', 'failed']
                    state_data_pub.workpoint = response.grasp[count]
                    sleep(3)
                    print(state_data_pub.workpoint)
                    self.state_data.publish(state_data_pub)
                    break

                elif response.state[i] == '450':
                    state_data_pub.statename = 'AfterAssemble'
                    state_data_pub.id = 'AfterAssemble'
                    state_data_pub.dst = ['success', 'failed']
                    sleep(3)
                    self.state_data.publish(state_data_pub)
                    break

                elif response.state[i] == '600':
                    state_data_pub.statename = 'FinalState'
                    state_data_pub.id = 'FinalState'
                    state_data_pub.dst = ['success', 'failed']
                    state_data_pub.is_end = True
                    sleep(3)
                    self.state_data.publish(state_data_pub)
                    break

        print('published')
        print(state_data_pub)


if __name__ == '__main__':
    rospy.init_node("state_data")
    publish = Publisher()
    publish.publisher_state_data()
    rospy.spin()
