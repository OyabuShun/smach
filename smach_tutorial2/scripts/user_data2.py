#!/usr/bin/env python

#import roslib; roslib.load_manifest('smach_tutorials')
import rospy
from smach import State, StateMachine
from smach_ros import IntrospectionServer
from time import sleep

# define state Foo


class Foo(State):
    def __init__(self):
        State.__init__(self, outcomes=['outcome1', 'outcome2'], input_keys=[
                       'foo_counter_in'], output_keys=['foo_counter_out'])

    def execute(self, userdata):
        rospy.loginfo('Executing state FOO')
        if userdata.foo_counter_in < 3:
            userdata.foo_counter_out = userdata.foo_counter_in + 1
            sleep(1)
            return 'outcome1'
        else:
            sleep(1)
            return 'outcome2'


# define state Bar
class Bar(State):
    def __init__(self):
        State.__init__(
            self,
            outcomes=['outcome1'],
            input_keys=['bar_counter_in'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAR')
        rospy.loginfo('Counter = %f' % userdata.bar_counter_in)
        sleep(1)
        return 'outcome1'


def main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm = StateMachine(outcomes=['outcome4'])
    sm.userdata.sm_counter = 0

    sis = IntrospectionServer('example', sm, '/SM_ROOT')
    sis.start()

    # Open the container
    with sm:
        # Add states to the container
        StateMachine.add(
            'FOO', Foo(), transitions={
                'outcome1': 'BAR', 'outcome2': 'outcome4'}, remapping={
                'foo_counter_in': 'sm_counter', 'foo_counter_out': 'sm_counter'})
        StateMachine.add(
            'BAR', Bar(), transitions={
                'outcome1': 'FOO'}, remapping={
                'bar_counter_in': 'sm_counter'})

    # Execute SMACH plan
    outcome = sm.execute()
    rospy.spin()


if __name__ == '__main__':
    main()
