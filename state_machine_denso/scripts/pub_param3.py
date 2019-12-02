#!/usr/bin/env python

import rospy
#from state_machine_denso.srv import WorkPointSrv, WorkPointSrvResponse
from denso_state_srvs.srv import WorkPointSrv, WorkPointSrvResponse


def handle_service(req):
    rospy.loginfo('called!')

    res = WorkPointSrvResponse()
    res.state = ['100', '200', '300']
    res.grasp.position.x = 0.5
    res.grasp.position.y = -0.3
    res.grasp.position.z = 0.3
    res.grasp.orientation.x = 1.0
    res.assemble.position.x = 0.5
    res.assemble.position.y = 0.3
    res.assemble.position.z = 0.3
    res.assemble.orientation.x = 1.0
    print(res)
    return res


def unity_service_server():
    rospy.init_node('service_server')
    s = rospy.Service('/state_data_service', WorkPointSrv, handle_service)
    print "Ready to service."
    rospy.spin()


if __name__ == '__main__':
    unity_service_server()
