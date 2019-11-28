#!/usr/bin/env python

import rospy
from state_machine_denso.msg import StateMachine_msgs
from time import sleep

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
