#!/usr/bin/env python

import rospy
from smach import State, StataMachine

class InitialState(State):
    def __init__(self, **kwargs):
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdate):
        pass
        return 'success'

class BeforeGrasp(State):
    def __init__(self, **kwargs):
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdate):
        pass
        return 'success'

class AfterGrasp(State):
    def __init__(self, **kwargs):
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdate):
        pass
        return 'success'

class BeforeAssemble(State):
    def __init__(self, **kwargs):
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdate):
        pass
        return 'success'

class AfterAssemble(State):
    def __init__(self, **kwargs):
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdate):
        pass
        return 'success'


class FinalState(State):
    def __init__(self, **kwargs):
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdate):
        pass
        return 'success'


