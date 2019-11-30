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
        state_data = StateMachine_msgs2()

        for i, name in enumerate(response.state):
            if response.state[i] == '100':
                response.state[i] = 'InitialState'
            elif response.state[i] == '200':
                response.state[i] = 'BeforeGrasp'
            elif response.state[i] == '300':
                response.state[i] = 'AfterGrasp'

        state_data.state = response.state
        print(state_data.state)

if __name__ == '__main__':
    rospy.init_node("state_date")
    publish = Publisher()
    publish.publisher_state_data()
    rospy.spin()

"""
rospy.init_node('pub_param')
pub = rospy.Publisher('state', StateMachine_msgs, queue_size=10)
sleep(1)

msg = StateMachine_msgs()
msg.id = 'InitialState1'
msg.statename = 'InitialState'
msg.src = ['success', 'failed']
msg.dst = ['BeforeGrasp', 'failed']
msg.is_end = False
pub.publish(msg)
sleep(1)

msg = StateMachine_msgs()
msg.id = 'BeforeGrasp'
msg.statename = 'BeforeGrasp'
msg.src = ['success', 'failed']
msg.dst = ['AfterGrasp', 'failed']
msg.is_end = False
pub.publish(msg)
sleep(1)

msg = StateMachine_msgs()
msg.id = 'AfterGrasp'
msg.statename = 'AfterGrasp'
msg.src = ['success', 'failed']
msg.dst = ['BeforeAssemble', 'failed']
msg.is_end = False
pub.publish(msg)
sleep(1)

msg = StateMachine_msgs()
msg.id = 'BeforeAssemble'
msg.statename = 'BeforeAssemble'
msg.src = ['success', 'failed']
msg.dst = ['AfterAssemble', 'failed']
msg.is_end = False
pub.publish(msg)
sleep(1)

msg = StateMachine_msgs()
msg.id = 'AfterAssemble'
msg.statename = 'AfterAssemble'
msg.src = ['success', 'failed']
msg.dst = ['FinalState', 'failed']
msg.is_end = False
pub.publish(msg)
sleep(1)

msg = StateMachine_msgs()
msg.id = 'FinalState'
msg.statename = 'FinalState'
msg.src = ['success', 'failed']
msg.dst = ['success', 'failed']

msg.keywords = ['sleeptime']
msg.args = ['3']
msg.is_end = True
pub.publish(msg)

print('---published---')
sleep(1)
print('Please press Ctlc-C')

while not rospy.is_shutdown():
    pass
"""
