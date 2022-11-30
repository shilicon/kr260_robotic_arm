import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image # Image is the message type

import cv2 # OpenCV library
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import numpy as np


class CannyEdgeDetection(Node):

    def __init__(self):
        super().__init__('canny_edge_detection')
        self.subscription = self.create_subscription(
            Image,
            '/image_raw',
            self.listener_callback,
            qos_profile_sensor_data)
        self.subscription  # prevent unused variable warning
        
        # Used to convert between ROS and OpenCV images
        self.br = CvBridge()

    def listener_callback(self, data):
        
        # Display the message on the console
        #self.get_logger().info('Receiving image')
        
        # Convert ROS Image message to OpenCV image
        frame = self.br.imgmsg_to_cv2(data, "bgr8")
        frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply Canny Edge Detection
        edges = cv2.Canny(frame_grayscale,100,200)
 
        # Display image
        cv2.imshow("Original Image", frame)
        cv2.imshow("Canny Edge Detection", edges)

        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)

    canny_edge_detection = CannyEdgeDetection()

    rclpy.spin(canny_edge_detection)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    canny_edge_detection.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()