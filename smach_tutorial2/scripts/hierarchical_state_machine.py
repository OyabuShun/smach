#!/usr/bin/env python

import rospy
from smach import State, StateMachine
from smach_ros import IntrospectionServer
from time import sleep

# define state Foo
class Foo(State):
    def __init__(self):
        State.__init__(self, outcomes=['outcome1', 'outcome2'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Executing state Foo')
        if self.counter < 3:
            self.counter += 1
            sleep(1)
            return 'outcome1'
        else:
            sleep(1)
            return 'outcome2'


# define state Bar
class Bar(State):
    def __init__(self):
        State.__init__(self, outcomes=['outcome1'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAR')
        sleep(1)
        return 'outcome1'


# define state Bas
class Bas(State):
    def __init__(self):
        State.__init__(self, outcomes=['outcome3'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAS')
        sleep(1)
        return 'outcome3'


def main():
    rospy.init_node('smach_example_hierarchical_state_machine')

    # Create the top level SMACH state machine
    sm_top = StateMachine(outcomes=['outcome5'])

    # Open the container
    with sm_top:
        StateMachine.add('BAS', Bas(), transitions={'outcome3': 'SUB'})

        # Create the sub SMACH state machine
        sm_sub = StateMachine(outcomes=['outcome4'])

        # Open the container
        with sm_sub:

            # Add state to the container
            StateMachine.add(
                'FOO',
                Foo(),
                transitions={
                    'outcome1': 'BAR',
                    'outcome2': 'outcome4'})
            StateMachine.add('BAR', Bar(), transitions={'outcome1': 'FOO'})
        StateMachine.add('SUB', sm_sub, transitions={'outcome4': 'outcome5'})

    sis = IntrospectionServer('example', sm_top, '/SM_STATEMACHINE')
    sis.start()

    # Execute SMACH plan
    outcome = sm_top.execute()
    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
