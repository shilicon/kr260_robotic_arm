import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image # Image is the message type

import cv2 # OpenCV library
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images


class QRCodeDetector(Node):

    def __init__(self):
        super().__init__('qrcode_detector')
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
        
        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()

        # detect and decode
        data, bbox, _ = detector.detectAndDecode(frame)

        # if there is a QR code
        #if bbox is not None:
        if data:
            print("[+] QR Code detected, data:", data)
            # display the image with lines
            bbox = bbox[0]
            for i in range(len(bbox)):
                pt1 = [int(val) for val in bbox[i]]
                pt2 = [int(val) for val in bbox[(i + 1) % len(bbox)]]
                cv2.line(frame, pt1, pt2, color=(255, 0, 0), thickness=3)
        
        # display the result
        cv2.imshow("Camera", frame)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)

    qrcode_detector = QRCodeDetector()

    rclpy.spin(qrcode_detector)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    qrcode_detector.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()