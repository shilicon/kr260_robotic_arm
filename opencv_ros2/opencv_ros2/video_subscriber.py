import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image # Image is the message type

import cv2 # OpenCV library
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import numpy as np




target_list=[]
#ser = serial.Serial("/dev/ttyUSB0",115200)
color_dist = {'red': {'Lower': np.array([156, 43, 46]), 'Upper': np.array([180, 255, 255])},
              'yellow': {'Lower': np.array([10, 43, 50]), 'Upper': np.array([35, 255, 255])},
              'green': {'Lower': np.array([70, 50, 50]), 'Upper': np.array([99, 255, 255])},
              'blue': {'Lower': np.array([100, 43, 46]), 'Upper': np.array([124, 255, 255])},
              }
#目标颜色
target_color = ['green','blue','red']
target_color1 = ['green']
target_color2 = ['blue']
target_color3 = ['red']
def good_thresh_img(img):
  gs_frame = cv2.GaussianBlur(img, (5, 5), 0)                     #高斯滤波
  hsv = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV)                 # 转化成HSV图像
  erode_hsv = cv2.erode(hsv, None, iterations=2)
  return erode_hsv

#定义一个识别目标颜色并处理的函数
def select_color_img(target_color,erode_hsv):
  for i in target_color:
    mask=cv2.inRange(erode_hsv,color_dist[i]['Lower'],color_dist[i]['Upper'])
    if(i==target_color[0]):
      inRange_hsv=cv2.bitwise_and(erode_hsv,erode_hsv,mask = mask)
    else:
      inRange_hsv1=cv2.bitwise_and(erode_hsv,erode_hsv,mask = mask)
      inRange_hsv=cv2.add(inRange_hsv,inRange_hsv1)
  return  inRange_hsv

#定义一个提取轮廓的函数
def extract_contour(final_inRange_hsv):
  inRange_gray = cv2.cvtColor(final_inRange_hsv,cv2.COLOR_BGR2GRAY)
  contours,hierarchy = cv2.findContours(inRange_gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
  return contours
    
#定义一个寻找目标并绘制外接矩形的函数
def find_target(contours,draw_img):
  for c in contours:
    if cv2.contourArea(c) < 1500:             #过滤掉较面积小的物体
      continue
    else:
      target_list.append(c)               #将面积较大的物体视为目标并存入目标列表
  for i in target_list:                       #绘制目标外接矩形
    rect = cv2.minAreaRect(i)
    box = cv2.boxPoints(rect)
    cv2.drawContours(draw_img, [np.int0(box)], -1, (0, 255, 255), 2)
  return draw_img

#定义一个绘制中心点坐标的函数
def draw_center(target_list,draw_img):
    center_x = 0
    center_y = 0
    for  c in target_list:
        M = cv2.moments(c)                   #计算中心点的x、y坐标
        center_x = int(M['m10']/M['m00'])
        center_y = int(M['m01']/M['m00'])
        #print('center_x:',center_x)
        #print('center_y:',center_y)
    
        cv2.circle(draw_img,(center_x,center_y),7,128,-1)#绘制中心点
        str1 = '(' + str(center_x)+ ',' +str(center_y) +')' #把坐标转化为字符串
        cv2.putText(draw_img,str1,(center_x-50,center_y+40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)#绘制坐标点位
    
    return draw_img





class VideoSubscriber(Node):

    def __init__(self):
        super().__init__('video_subscriber')
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
        self.get_logger().info('Receiving image')
        
        # Convert ROS Image message to OpenCV image
        frame = self.br.imgmsg_to_cv2(data, "bgr8")
        img = frame
        img = img[0:680,250:600]
        global target_list
        target_list=[]
         
        
        erode_hsv = good_thresh_img(img)
        final_inRange_hsv = select_color_img(target_color,erode_hsv)
        draw_img = final_inRange_hsv
        contours = extract_contour(final_inRange_hsv)
        draw_img = find_target(contours,draw_img)
        final_img = draw_center(target_list,draw_img)
        
        # Display image
        cv2.imshow("camera", final_img)
        
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)

    video_subscriber = VideoSubscriber()

    rclpy.spin(video_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    video_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
