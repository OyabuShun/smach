#!/usr/bin/env python

import rospy
from smach import State, StateMachine, Concurrence
from smach_ros import IntrospectionServer
from time import sleep


class Foo(State):
    def __init__(self):
        State.__init__(self, outcomes=['outcome1', 'outcome2'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Executing state FOO')
        if self.counter < 3:
            self.counter += 1
            sleep(1)
            return 'outcome1'
        else:
            sleep(1)
            return 'outcome2'


class Bar(State):
    def __init__(self):
        State.__init__(self, outcomes=['outcome1'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAR')
        sleep(1)
        return 'outcome1'


class Bas(State):
    def __init__(self):
        State.__init__(self, outcomes=['outcome3'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAS')
        sleep(1)
        return 'outcome3'


def main():
    rospy.init_node('smach_example_state_machine')

    # Create the top level SMACH state machine
    sm_top = StateMachine(outcomes=['outcome6'])

    # Open the countainer
    with sm_top:
        StateMachine.add('BAS', Bas(), transitions={'outcome3': 'CON'})

        # Create the sub SMACH state machine
        sm_con = Concurrence(
            outcomes=[
                'outcome4',
                'outcome5'],
            default_outcome='outcome4',
            outcome_map={
                'outcome5': {
                    'FOO': 'outcome2',
                    'BAR': 'outcome1'}})

        # Open the countainer
        with sm_con:

            # Add states to the container
            Concurrence.add('FOO', Foo())
            Concurrence.add('BAR', Bar())

        StateMachine.add(
            'CON',
            sm_con,
            transitions={
                'outcome4': 'CON',
                'outcome5': 'outcome6'})

    sis = IntrospectionServer('example', sm_top, '/SM_PATH')
    sis.start()

    # Execute SMACH plan
    outcome = sm_top.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
