import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image # Image is the message type

import cv2 # OpenCV library
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import time


class TakePhoto(Node):

    def __init__(self):
        super().__init__('take_photo')
        self.subscription = self.create_subscription(
            Image,
            '/image',
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

        # Display image
        cv2.imshow("Camera", frame)
        
        key = cv2.waitKey(1) & 0xFF

        if key == ord("s"):
            # Save a photo
            # Use '_image_title' parameter from command line
            # Default value is 'photo.jpg'
            #img_title = rospy.get_param('~image_title', 'photo.jpg')
            timestr = time.strftime("%Y%m%d-%H%M%S-")
            img_title = timestr + "photo.jpg"

            cv2.imwrite(img_title, frame)
            print("Saved image " + img_title)


def main(args=None):
    rclpy.init(args=args)

    take_photo = TakePhoto()

    print("Press 's' to save image as a file in the current directory.")

    rclpy.spin(take_photo)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    take_photo.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()