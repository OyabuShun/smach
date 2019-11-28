#!/usr/bin/env python

import rospy
from smach import State, StateMachine
from time import sleep
from random import random


class InitialState(State):
    def __init__(self, **kwargs):
        self.sleeptime = 1
        try:
            self.sleeptime = int(kwargs['sleeptime'])
        except KeyError:
            pass
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        print('InitialState')
        sleep(self.sleeptime)
        a = 1
        if a >= 1:
            print('sucessssss')
            a += 1
            print(a)
            sleep(1)
            return 'success'
        else:
            sleep(1)
            return 'failed'


class BeforeGrasp(State):
    def __init__(self, **kwargs):
        self.sleeptime = 1
        try:
            self.sleeptime = int(kwargs['sleeptime'])
        except KeyError:
            pass
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        print('InitialState')
        sleep(self.sleeptime)
        if random() > 0.1:
            print('sucessssss')
            sleep(1)
            return 'success'
        else:
            sleep(1)
            return 'failed'


class AfterGrasp(State):
    def __init__(self, **kwargs):
        self.sleeptime = 1
        try:
            self.sleeptime = int(kwargs['sleeptime'])
        except KeyError:
            pass
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        print('InitialState')
        sleep(self.sleeptime)
        if random() > 0.6:
            print('sucessssss')
            sleep(1)
            return 'success'
        else:
            sleep(1)
            return 'failed'


class BeforeAssemble(State):
    def __init__(self, **kwargs):
        self.sleeptime = 1
        try:
            self.sleeptime = int(kwargs['sleeptime'])
        except KeyError:
            pass
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        print('InitialState')
        sleep(self.sleeptime)
        if random() > 0.6:
            print('sucessssss')
            sleep(1)
            return 'success'
        else:
            sleep(1)
            return 'failed'


class AfterAssemble(State):
    def __init__(self, **kwargs):
        self.sleeptime = 1
        try:
            self.sleeptime = int(kwargs['sleeptime'])
        except KeyError:
            pass
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        print('InitialState')
        sleep(self.sleeptime)
        if random() > 0.6:
            print('sucessssss')
            sleep(1)
            return 'success'
        else:
            sleep(1)
            return 'failed'


class FinalState(State):
    def __init__(self, **kwargs):
        self.sleeptime = 1
        try:
            self.sleeptime = int(kwargs['sleeptime'])
        except KeyError:
            pass
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        print('InitialState')
        sleep(self.sleeptime)
        if random() > 0.6:
            print('sucessssss')
            sleep(1)
            return 'success'
        else:
            sleep(1)
            return 'failed'
