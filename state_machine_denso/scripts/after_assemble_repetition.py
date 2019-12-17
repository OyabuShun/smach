#!/usr/bin/env python

import copy
from geometry_msgs.msg import PoseStamped
from smach import State
from denso_state_behavior import MovingBehavior


class AfterAssembleRepetition(State):
    """define AfterAssembleRepetition state"""

    def __init__(self, target, z_offset=0.10):
        """
        Parameters
        ----------
        target : geometry_msgs/PoseStamped
            target point of robot
        z_offset : float, default 0.10[m]
            z-axis offset value for approach/depart moving
        """
        State.__init__(self, outcomes=['success', 'failed'])
        if not isinstance(target, PoseStamped):
            raise TypeError(
                'target must be a type of geometry_msgs/PoseStamped')
        self.target = target
        self.z_offset = z_offset

    def execute(self, userdata):
        offset_target = copy.deepcopy(self.target)
        offset_target.position.z -= self.z_offset

        moving_obj = MovingBehavior(self.target)
        offset_moving_obj = MovingBehavior(offset_target)

        ret = moving_obj.execute_impl()
        if ret == 'failed':
            return 'failed'

        ret = offset_moving_obj.execute_impl()
        if ret == 'failed':
            return 'failed'

        return 'success'
