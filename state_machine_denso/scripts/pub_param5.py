#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Pose
#from state_machine_denso.srv import WorkPointSrv, WorkPointSrvResponse
from denso_state_srvs.srv import WorkPointSrv, WorkPointSrvResponse
from denso_state_srvs.srv import WorkPointServiceProvider, WorkPointServiceProviderResponse


def handle_service(req):
    rospy.loginfo('called!')

    res = WorkPointServiceProviderResponse()
    grasp_pose = Pose()
    grasp_pose2 = Pose()
    grasp_pose3 = Pose()
    grasp_pose4 = Pose()
    grasp_pose5 = Pose()
    grasp_pose6 = Pose()
    assemble_pose = Pose()
    assemble_pose2 = Pose()
    assemble_pose3 = Pose()
    assemble_pose4 = Pose()
    assemble_pose5 = Pose()
    assemble_pose6 = Pose()
    res.state = [
        '100',
        '200',
        '300',
        '400',
        '500',
        '200',
        '300',
        '400',
        '500',
        '600']
    #res.state = ['100', '200', '300', '400', '500', '600']

    grasp_pose.position.x = 0.5
    grasp_pose.position.y = -0.3
    grasp_pose.position.z = 0.3
    grasp_pose.orientation.x = 1.0
    print(type(grasp_pose))
    res.grasp.append(grasp_pose)

    grasp_pose2.position.x = 0.5
    grasp_pose2.position.y = -0.3
    grasp_pose2.position.z = 0.3
    grasp_pose2.orientation.x = 1.0

    res.grasp.append(grasp_pose2)

    grasp_pose3.position.x = 0.5
    grasp_pose3.position.y = -0.3
    grasp_pose3.position.z = 0.3
    grasp_pose3.orientation.x = 1.0

    res.grasp.append(grasp_pose3)

    grasp_pose4.position.x = 0.5
    grasp_pose4.position.y = -0.3
    grasp_pose4.position.z = 0.3
    grasp_pose4.orientation.x = 1.0

    res.grasp.append(grasp_pose4)

    grasp_pose5.position.x = 0.5
    grasp_pose5.position.y = -0.3
    grasp_pose5.position.z = 0.3
    grasp_pose5.orientation.x = 1.0

    res.grasp.append(grasp_pose5)

    grasp_pose6.position.x = 0.5
    grasp_pose6.position.y = -0.3
    grasp_pose6.position.z = 0.3
    grasp_pose6.orientation.x = 1.0

    res.grasp.append(grasp_pose6)

    assemble_pose.position.x = 0.5
    assemble_pose.position.y = 0.3
    assemble_pose.position.z = 0.3
    assemble_pose.orientation.x = 1.0

    res.assemble.append(assemble_pose)

    assemble_pose2.position.x = 0.5
    assemble_pose2.position.y = 0.3
    assemble_pose2.position.z = 0.3
    assemble_pose2.orientation.x = 1.0

    res.assemble.append(assemble_pose2)

    assemble_pose3.position.x = 0.5
    assemble_pose3.position.y = 0.3
    assemble_pose3.position.z = 0.3
    assemble_pose3.orientation.x = 1.0

    res.assemble.append(assemble_pose3)

    assemble_pose4.position.x = 0.5
    assemble_pose4.position.y = 0.3
    assemble_pose4.position.z = 0.3
    assemble_pose4.orientation.x = 1.0

    res.assemble.append(assemble_pose4)

    assemble_pose5.position.x = 0.5
    assemble_pose5.position.y = 0.3
    assemble_pose5.position.z = 0.3
    assemble_pose5.orientation.x = 1.0

    res.assemble.append(assemble_pose5)

    assemble_pose6.position.x = 0.5
    assemble_pose6.position.y = 0.3
    assemble_pose6.position.z = 0.3
    assemble_pose6.orientation.x = 1.0

    res.assemble.append(assemble_pose6)

    print(res)
    return res


def unity_service_server():
    rospy.init_node('service_server')
    #s = rospy.Service('/state_data_service', WorkPointSrv, handle_service)
    s = rospy.Service('/test', WorkPointServiceProvider, handle_service)
    print "Ready to service."
    rospy.spin()


if __name__ == '__main__':
    unity_service_server()
