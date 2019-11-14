#!/usr/bin/env python

from geometry_msgs.msg import PoseStamped
from smach import State
from denso_state_behavior import *
from denso_state_smach import *


class ErrorHandlingState(State):
    """define ErrorHandlingState state"""

    def __init__(self):
        State.__init__(self, outcomes=['success', 'failed'])

    def execute(self, userdata):
        init_moving_obj = MovingBehavior(InitialState._get_initial_pose())

        ret = init_moving_obj.execute_impl()
        if ret == 'failed':
            return 'failed'

        return 'success'
