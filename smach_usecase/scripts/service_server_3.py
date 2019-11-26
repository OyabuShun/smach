#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse

def handle_service(req):
    rospy.loginfo('called')
    return EmptyResponse()

def service_server():
    rospy.init_node('service')
    s = rospy.Service('/reset', Empty, handle_service)
    print('Ready to service')
    rospy.spin()


if __name__ == '__main__':
    service_server()
