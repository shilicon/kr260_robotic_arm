# Basics ROS 2 program to subscribe to real-time streaming 
# video from RGB-D sensor
# Author:
# - Jeffrey
# - https://github.com/jeffreyttc
  
# Import the necessary libraries
import rclpy # Python library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library
import serial 
import time
import numpy as np
# Load the cascade
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
 

from rclpy.qos import qos_profile_sensor_data
target_list=[]

target_list11=[]
target_list12=[]
target_list13=[]
target_list21=[]
target_list22=[]
target_list23=[]
target_list31=[]
target_list32=[]
target_list33=[]

ser = serial.Serial("/dev/ttyUSB0",115200)
color_dist = {'red': {'Lower': np.array([156, 43, 46]), 'Upper': np.array([180, 255, 255])},
              'yellow': {'Lower': np.array([10, 43, 50]), 'Upper': np.array([35, 255, 255])},
              'green': {'Lower': np.array([70, 50, 50]), 'Upper': np.array([99, 255, 255])},
              'blue': {'Lower': np.array([100, 43, 46]), 'Upper': np.array([124, 255, 255])},
              }
#目标颜色
target_color = ['green','blue','red','yellow']
target_color1 = ['green']
target_color2 = ['blue']
target_color3 = ['red']
target_color4 = ['yellow']

def arm_init():
  a = 0.5;
  print('begin')
  ser.write(b'#005P1200T1000!\n\r')
  time.sleep(a)
  ser.write(b'#004P1500T1000!\n\r')
  time.sleep(a)
  ser.write(b'#003P1000T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P1500T1000!\n\r')
  time.sleep(a)
  ser.write(b'#001P1970T1000!\n\r')
  time.sleep(a)
  ser.write(b'#000P1300T1000!\n\r')
  time.sleep(a)

  print('end')
    #return ()

def arm_first_body_catch():
  a = 0.4;
  print('begin')
  ser.write(b'#000P1600T1000!\n\r')
  time.sleep(a)
  ser.write(b'#001P2200T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P0900T1000!\n\r')
  time.sleep(a)
  ser.write(b'#003P0800T1000!\n\r')
  time.sleep(a)
#ser.write(b'#004P1500T1000!\n\r')
#time.sleep(a)
  ser.write(b'#005P1400T1000!\n\r')
  time.sleep(a)
  print('second')
  ser.write(b'#000P1830T1000!\n\r')
  time.sleep(a)
  ser.write(b'#001P2450T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P1050T1000!\n\r')
  time.sleep(a)
  ser.write(b'#003P1000T1000!\n\r')
  time.sleep(a)
#ser.write(b'#004P1500T1000!\n\r')
#time.sleep(a)
  ser.write(b'#005P1100T1000!\n\r')
  time.sleep(1)
  print('end')
  return 0

def arm_first_body_init():
  a = 0.4;

#ser.write(b'#004P1500T1000!\n\r')
#time.sleep(1)
  #ser.write(b'#005P1100T1000!\n\r')
 # time.sleep(a)
  ser.write(b'#003P1000T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P1400T1000!\n\r')
  time.sleep(a)
  ser.write(b'#000P1300T1000!\n\r')
  time.sleep(a)
  ser.write(b'#001P2000T1000!\n\r')
  time.sleep(a)
  print('end')
  return 0

def arm_first_body_down():
    a=0.4
    print('begin')

    ser.write(b'#000P0900T1000!\n\r')
    time.sleep(a)
    ser.write(b'#001P2100T1000!\n\r')
    time.sleep(a)
    ser.write(b'#002P1000T1000!\n\r')
    time.sleep(a)
    ser.write(b'#003P1200T1000!\n\r')
    time.sleep(a)
#ser.write(b'#004P1500T1000!\n\r')
#time.sleep(a)
    ser.write(b'#005P1100T1000!\n\r')
    time.sleep(a)
    print('third')
#ser.write(b'#000P0600T1000!\n\r')
#time.sleep(a)
    ser.write(b'#001P2350T1000!\n\r')
    time.sleep(a)
#ser.write(b'#002P1000T1000!\n\r')
#time.sleep(a)
#ser.write(b'#003P1200T1000!\n\r')
#time.sleep(a)
#ser.write(b'#004P1500T1000!\n\r')
#time.sleep(a)
    ser.write(b'#005P1400T1000!\n\r')
    time.sleep(a)
    print('end')
    return 0


def arm_third_body_catch():
  a = 0.5
  print('begin')
  ser.write(b'#000P2100T1000!\n\r')
  time.sleep(a)
  ser.write(b'#001P2200T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P1000T1000!\n\r')
  time.sleep(a)
  ser.write(b'#003P1100T1000!\n\r')
  time.sleep(a)
  #ser.write(b'#004P1500T1000!\n\r')
  #time.sleep(a)
  ser.write(b'#005P1300T1000!\n\r')
  time.sleep(a)
  print('second')
  #ser.write(b'#000P1900T1000!\n\r')
  #time.sleep(a)
  ser.write(b'#003P0900T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P1100T1000!\n\r')
  time.sleep(a)
  ser.write(b'#001P2450T1000!\n\r')
  time.sleep(a)
#ser.write(b'#004P1500T1000!\n\r')
#time.sleep(a)
  print('third')
  ser.write(b'#002P0650T1000!\n\r')
  time.sleep(a)
  ser.write(b'#003P0500T1000!\n\r')
  time.sleep(0.5)
  ser.write(b'#005P1100T1000!\n\r')
  time.sleep(1)
  print('end')

def arm_third_body_init():
  a = 0.4;
  print('begin')

  #ser.write(b'#004P1500T1000!\n\r')
  #time.sleep(1)
  ser.write(b'#001P2000T1000!\n\r')
  time.sleep(a)
  #ser.write(b'#005P1170T1000!\n\r')
  #time.sleep(a)
  ser.write(b'#003P1000T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P1400T1000!\n\r')
  time.sleep(a)
  ser.write(b'#000P1300T1000!\n\r')
  time.sleep(a)

  print('end')


def arm_third_body_down():

  a = 0.5;
  print('begin')

  ser.write(b'#000P0500T1000!\n\r')
  time.sleep(a)
  ser.write(b'#001P2400T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P1200T1000!\n\r')
  time.sleep(a)
  ser.write(b'#003P1200T1000!\n\r')
  time.sleep(a)
#ser.write(b'#004P1500T1000!\n\r')
#time.sleep(a)
  ser.write(b'#005P1300T1000!\n\r')
  time.sleep(a) 
  print('end')

def arm_third_init():
#ARM init after moving
  a = 0.5;
  print('begin')
  ser.write(b'#005P1200T1000!\n\r')
  #ser.write(b'#004P1500T1000!\n\r')
  time.sleep(a)
  ser.write(b'#003P1000T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P1500T1000!\n\r')
  time.sleep(a)
  ser.write(b'#001P2000T1000!\n\r')
  time.sleep(a)
  ser.write(b'#000P1300T1000!\n\r')
  time.sleep(a)
  print('end')


def arm_second_init():
  a = 0.5
  ser.write(b'#005P1400T1000!\n\r')
  time.sleep(a)
  ser.write(b'#004P1500T1000!\n\r')
  time.sleep(a)
  ser.write(b'#003P1000T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P1500T1000!\n\r')
  time.sleep(a)
  ser.write(b'#001P2000T1000!\n\r')
  time.sleep(a)
  ser.write(b'#000P1300T1000!\n\r')
  time.sleep(a)

  print('end')

def arm_second_catch():

  a = 0.4
  print('begin')
  ser.write(b'#000P2000T1000!\n\r')
  time.sleep(a)
  ser.write(b'#001P2200T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P0900T1000!\n\r')
  time.sleep(a)
  ser.write(b'#003P0800T1000!\n\r')
  time.sleep(a)
 # ser.write(b'#004P1500T1000!\n\r')
  #time.sleep(a)
  ser.write(b'#005P1400T1000!\n\r')
  time.sleep(a)
  print('second')
  #ser.write(b'#000P1830T1000!\n\r')
  #time.sleep(a)
  ser.write(b'#001P2400T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P1050T1000!\n\r')
  time.sleep(a)
  ser.write(b'#003P1100T1000!\n\r')
  time.sleep(0.5)
#ser.write(b'#004P1500T1000!\n\r')
#time.sleep(a)
  ser.write(b'#005P1100T1000!\n\r')
  time.sleep(1)
  print('end')
 
def arm_second_body():
  a = 0.4  
  print('begin')

#ser.write(b'#004P1500T1000!\n\r')
#time.sleep(1)
#ser.write(b'#005P1170T1000!\n\r')
#time.sleep(a)
  ser.write(b'#003P1000T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P1400T1000!\n\r')
  time.sleep(a)
  ser.write(b'#000P1300T1000!\n\r')
  time.sleep(a)
  ser.write(b'#001P2000T1000!\n\r')
  time.sleep(a)
  print('end') 
  
  
def arm_second_body_down():
  a = 0.5 
  ser.write(b'#000P0700T1000!\n\r')
  time.sleep(a)
  ser.write(b'#001P2100T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P1000T1000!\n\r')
  time.sleep(a)
  ser.write(b'#003P1200T1000!\n\r')
  time.sleep(a)
#ser.write(b'#004P1500T1000!\n\r')
#time.sleep(a)
#ser.write(b'#005P1170T1000!\n\r')
#time.sleep(a)
  print('third')
  ser.write(b'#000P0700T1000!\n\r')
  time.sleep(a)
  ser.write(b'#001P2350T1000!\n\r')
  time.sleep(a)
#ser.write(b'#002P1000T1000!\n\r')
#time.sleep(a)
#ser.write(b'#003P1200T1000!\n\r')
#time.sleep(a)
#ser.write(b'#004P1500T1000!\n\r')
#time.sleep(a)
  ser.write(b'#005P1400T1000!\n\r')
  time.sleep(a)

  print('end')  

def arm_second_init2():
  a = 0.5  
  print('begin')
  ser.write(b'#005P1400T1000!\n\r')
  time.sleep(a)
  ser.write(b'#004P1500T1000!\n\r')
  time.sleep(a)
  ser.write(b'#003P1000T1000!\n\r')
  time.sleep(a)
  ser.write(b'#002P1500T1000!\n\r')
  time.sleep(a)
  ser.write(b'#001P2000T1000!\n\r')
  time.sleep(a)
  ser.write(b'#000P1300T1000!\n\r')
  time.sleep(a)
  print('end')  
                                                                     
obj = False

def good_thresh_img(img):
  gs_frame = cv2.GaussianBlur(img, (5, 5), 0)                     #高斯滤波
  hsv = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV)                 # 转化成HSV图像
  erode_hsv = cv2.erode(hsv, None, iterations=2)
  k = np.ones((3,3),np.uint8)
  erode_hsv = cv2.erode(erode_hsv,k,iterations=3)
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

def select_color_blue(target_color,erode_hsv):
  for i in target_color:
    mask=cv2.inRange(erode_hsv,color_dist[i]['Lower'],color_dist[i]['Upper'])
    if(i==target_color[0]):
      inRange_hsv=cv2.bitwise_and(erode_hsv,erode_hsv,mask = mask)
    else:
      inRange_hsv1=cv2.bitwise_and(erode_hsv,erode_hsv,mask = mask)
      inRange_hsv=cv2.add(inRange_hsv,inRange_hsv1)
  return  inRange_hsv 


def select_color_red(target_color,erode_hsv):
  for i in target_color:
    mask=cv2.inRange(erode_hsv,color_dist[i]['Lower'],color_dist[i]['Upper'])
    if(i==target_color[0]):
      inRange_hsv=cv2.bitwise_and(erode_hsv,erode_hsv,mask = mask)
    else:
      inRange_hsv1=cv2.bitwise_and(erode_hsv,erode_hsv,mask = mask)
      inRange_hsv=cv2.add(inRange_hsv,inRange_hsv1)
  return  inRange_hsv 

def select_color_green(target_color,erode_hsv):
  for i in target_color:
    mask=cv2.inRange(erode_hsv,color_dist[i]['Lower'],color_dist[i]['Upper'])
  if(i==target_color[0]):
    inRange_hsv=cv2.bitwise_and(erode_hsv,erode_hsv,mask = mask)
  else:
    inRange_hsv1=cv2.bitwise_and(erode_hsv,erode_hsv,mask = mask)
    inRange_hsv=cv2.add(inRange_hsv,inRange_hsv1)
  return  inRange_hsv

def select_color_yellow(target_color,erode_hsv):
  for i in target_color:
    mask=cv2.inRange(erode_hsv,color_dist[i]['Lower'],color_dist[i]['Upper'])
    if(i==target_color[0]):
      inRange_hsv=cv2.bitwise_and(erode_hsv,erode_hsv,mask = mask)
    else:
      inRange_hsv1=cv2.bitwise_and(erode_hsv,erode_hsv,mask = mask)
      inRange_hsv=cv2.add(inRange_hsv,inRange_hsv1)
  return  inRange_hsv 

def find_target11(contours,draw_img):
  for c in contours:
      if cv2.contourArea(c) < 500:             #过滤掉较面积小的物体
         continue
      else:
         target_list11.append(c)               #将面积较大的物体视为目标并存入目标列表
  for i in target_list11:                       #绘制目标外接矩形
      rect = cv2.minAreaRect(i)
      box = cv2.boxPoints(rect)
      cv2.drawContours(draw_img, [np.int0(box)], -1, (0, 255, 255), 2)
  return draw_img



def find_target12(contours,draw_img):
  for c in contours:
      if cv2.contourArea(c) < 500:             #过滤掉较面积小的物体
         continue
      else:
         target_list12.append(c)               #将面积较大的物体视为目标并存入目标列表
  for i in target_list12:                       #绘制目标外接矩形
      rect = cv2.minAreaRect(i)
      box = cv2.boxPoints(rect)
      cv2.drawContours(draw_img, [np.int0(box)], -1, (0, 255, 255), 2)
  return draw_img

def find_target13(contours,draw_img):
  for c in contours:
      if cv2.contourArea(c) < 500:             #过滤掉较面积小的物体
         continue
      else:
         target_list13.append(c)               #将面积较大的物体视为目标并存入目标列表
  for i in target_list13:                       #绘制目标外接矩形
      rect = cv2.minAreaRect(i)
      box = cv2.boxPoints(rect)
      cv2.drawContours(draw_img, [np.int0(box)], -1, (0, 255, 255), 2)
  return draw_img

def find_target21(contours,draw_img):
    for c in contours:
        if cv2.contourArea(c) < 1500:             #过滤掉较面积小的物体
            continue
        else:
            target_list21.append(c)               #将面积较大的物体视为目标并存入目标列表
    for i in target_list21:                       #绘制目标外接矩形
        rect = cv2.minAreaRect(i)
        box = cv2.boxPoints(rect)
        cv2.drawContours(draw_img, [np.int0(box)], -1, (0, 255, 255), 2)
    return draw_img

def find_target22(contours,draw_img):
  for c in contours:
      if cv2.contourArea(c) < 1000:             #过滤掉较面积小的物体
         continue
      else:
         target_list22.append(c)               #将面积较大的物体视为目标并存入目标列表
  for i in target_list22:                       #绘制目标外接矩形
      rect = cv2.minAreaRect(i)
      box = cv2.boxPoints(rect)
      cv2.drawContours(draw_img, [np.int0(box)], -1, (0, 255, 255), 2)
  return draw_img

def find_target23(contours,draw_img):
  for c in contours:
      if cv2.contourArea(c) < 1500:             #过滤掉较面积小的物体
         continue
      else:
         target_list23.append(c)               #将面积较大的物体视为目标并存入目标列表
  for i in target_list23:                       #绘制目标外接矩形
      rect = cv2.minAreaRect(i)
      box = cv2.boxPoints(rect)
      cv2.drawContours(draw_img, [np.int0(box)], -1, (0, 255, 255), 2)
  return draw_img

def find_target31(contours,draw_img):
  for c in contours:
      if cv2.contourArea(c) < 1500:             #过滤掉较面积小的物体
         continue
      else:
         target_list31.append(c)               #将面积较大的物体视为目标并存入目标列表
  for i in target_list31:                       #绘制目标外接矩形
      rect = cv2.minAreaRect(i)
      box = cv2.boxPoints(rect)
      cv2.drawContours(draw_img, [np.int0(box)], -1, (0, 255, 255), 2)
  return draw_img

def find_target32(contours,draw_img):
  for c in contours:
      if cv2.contourArea(c) < 1000:             #过滤掉较面积小的物体
         continue
      else:
         target_list32.append(c)               #将面积较大的物体视为目标并存入目标列表
  for i in target_list32:                       #绘制目标外接矩形
      rect = cv2.minAreaRect(i)
      box = cv2.boxPoints(rect)
      cv2.drawContours(draw_img, [np.int0(box)], -1, (0, 255, 255), 2)
  return draw_img

def find_target33(contours,draw_img):
  for c in contours:
      if cv2.contourArea(c) < 1500:             #过滤掉较面积小的物体
         continue
      else:
         target_list33.append(c)               #将面积较大的物体视为目标并存入目标列表
  for i in target_list33:                       #绘制目标外接矩形
      rect = cv2.minAreaRect(i)
      box = cv2.boxPoints(rect)
      cv2.drawContours(draw_img, [np.int0(box)], -1, (0, 255, 255), 2)
  return draw_img

def draw_center11(target_list11,draw_img):
  center_x11 = 0
  center_y11 = 0
  for c in target_list11:
      M = cv2.moments(c)                   #计算中心点的x、y坐标
      center_x11 = int(M['m10']/M['m00'])
      center_y11 = int(M['m01']/M['m00'])
      print('center_x11:',center_x11)
      print('center_y11:',center_y11)
    
      cv2.circle(draw_img,(center_x11,center_y11),7,128,-1)#绘制中心点
      str1 = '(' + str(center_x11)+ ',' +str(center_y11) +')' #把坐标转化为字符串
      cv2.putText(draw_img,str1,(center_x11-50,center_y11+40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)#绘制坐标点位
    
  return draw_img,center_x11,center_y11

def draw_center12(target_list12,draw_img):
  center_x12 = 0
  center_y12 = 0
  for c in target_list12:
      M = cv2.moments(c)                   #计算中心点的x、y坐标
      center_x12 = int(M['m10']/M['m00'])
      center_y12 = int(M['m01']/M['m00'])
      print('center_x12:',center_x12)
      print('center_y12:',center_y12)
    
      cv2.circle(draw_img,(center_x12,center_y12),7,128,-1)#绘制中心点
      str1 = '(' + str(center_x12)+ ',' +str(center_y12) +')' #把坐标转化为字符串
      cv2.putText(draw_img,str1,(center_x12-50,center_y12+40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)#绘制坐标点位
    
  return draw_img,center_x12,center_y12

def draw_center13(target_list13,draw_img):
  center_x13 = 0
  center_y13 = 0
  for c in target_list13:
      M = cv2.moments(c)                   #计算中心点的x、y坐标
      center_x13 = int(M['m10']/M['m00'])
      center_y13 = int(M['m01']/M['m00'])
      print('center_x13:',center_x13)
      print('center_y13:',center_y13)
    
      cv2.circle(draw_img,(center_x13,center_y13),7,128,-1)#绘制中心点
      str1 = '(' + str(center_x13)+ ',' +str(center_y13) +')' #把坐标转化为字符串
      cv2.putText(draw_img,str1,(center_x13-50,center_y13+40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)#绘制坐标点位
    
  return draw_img,center_x13,center_y13

def draw_center23(target_list23,draw_img):
  center_x23 = 0
  center_y23 = 0
  for c in target_list23:
      M = cv2.moments(c)                   #计算中心点的x、y坐标
      center_x23 = int(M['m10']/M['m00'])
      center_y23 = int(M['m01']/M['m00'])
      print('center_x23:',center_x23)
      print('center_y23:',center_y23)
    
      cv2.circle(draw_img,(center_x23,center_y23),7,128,-1)#绘制中心点
      str1 = '(' + str(center_x23)+ ',' +str(center_y23) +')' #把坐标转化为字符串
      cv2.putText(draw_img,str1,(center_x23-50,center_y23+40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)#绘制坐标点位
    
  return draw_img,center_x23,center_y23

def draw_center21(target_list21,draw_img):
  center_x21 = 0
  center_y21 = 0
  for c in target_list21:
      M = cv2.moments(c)                   #计算中心点的x、y坐标
      center_x21 = int(M['m10']/M['m00'])
      center_y21 = int(M['m01']/M['m00'])
      print('center_x21:',center_x21)
      print('center_y21:',center_y21)
    
      cv2.circle(draw_img,(center_x21,center_y21),7,128,-1)#绘制中心点
      str1 = '(' + str(center_x21)+ ',' +str(center_y21) +')' #把坐标转化为字符串
      cv2.putText(draw_img,str1,(center_x21-50,center_y21+40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)#绘制坐标点位
    
  return draw_img,center_x21,center_y21

def draw_center22(target_list22,draw_img):
  center_x22 = 0
  center_y22 = 0
  for c in target_list22:
      M = cv2.moments(c)                   #计算中心点的x、y坐标
      center_x22 = int(M['m10']/M['m00'])
      center_y22 = int(M['m01']/M['m00'])
      print('center_x22:',center_x22)
      print('center_y22:',center_y22)
    
      cv2.circle(draw_img,(center_x22,center_y22),7,128,-1)#绘制中心点
      str1 = '(' + str(center_x22)+ ',' +str(center_y22) +')' #把坐标转化为字符串
      cv2.putText(draw_img,str1,(center_x22-50,center_y22+40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)#绘制坐标点位
    
  return draw_img,center_x22,center_y22

def draw_center31(target_list31,draw_img):
  center_x31 = 0
  center_y31 = 0
  for c in target_list31:
      M = cv2.moments(c)                   #计算中心点的x、y坐标
      center_x31 = int(M['m10']/M['m00'])
      center_y31 = int(M['m01']/M['m00'])
      print('center_x31:',center_x31)
      print('center_y31:',center_y31)
    
      cv2.circle(draw_img,(center_x31,center_y31),7,128,-1)#绘制中心点
      str1 = '(' + str(center_x31)+ ',' +str(center_y31) +')' #把坐标转化为字符串
      cv2.putText(draw_img,str1,(center_x31-50,center_y31+40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)#绘制坐标点位
    
  return draw_img,center_x31,center_y31

def draw_center32(target_list32,draw_img):
  center_x32 = 0
  center_y32 = 0
  for c in target_list32:
      M = cv2.moments(c)                   #计算中心点的x、y坐标
      center_x32 = int(M['m10']/M['m00'])
      center_y32 = int(M['m01']/M['m00'])
      print('center_x:',center_x32)
      print('center_y:',center_y32)
    
      cv2.circle(draw_img,(center_x32,center_y32),7,128,-1)#绘制中心点
      str1 = '(' + str(center_x32)+ ',' +str(center_y32) +')' #把坐标转化为字符串
      cv2.putText(draw_img,str1,(center_x32-50,center_y32+40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)#绘制坐标点位
    
  return draw_img,center_x32,center_y32

def draw_center33(target_list33,draw_img):
  center_x33 = 0
  center_y33 = 0
  for c in target_list33:
      M = cv2.moments(c)                   #计算中心点的x、y坐标
      center_x33 = int(M['m10']/M['m00'])
      center_y33 = int(M['m01']/M['m00'])
      print('center_x33:',center_x33)
      print('center_y33:',center_y33)
    
      cv2.circle(draw_img,(center_x33,center_y33),7,128,-1)#绘制中心点
      str1 = '(' + str(center_x33)+ ',' +str(center_y33) +')' #把坐标转化为字符串
      cv2.putText(draw_img,str1,(center_x33-50,center_y33+40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)#绘制坐标点位
    
  return draw_img,center_x33,center_y33







#定义一个提取轮廓的函数
def extract_contour(final_inRange_hsv):
  inRange_gray = cv2.cvtColor(final_inRange_hsv,cv2.COLOR_BGR2GRAY)
  contours,hierarchy = cv2.findContours(inRange_gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
  #global obj
  #if contours is not False: obj = ture
  
  #print(contours)
  return contours 
    
#定义一个寻找目标并绘制外接矩形的函数
def find_target(contours,draw_img):
  for c in contours:
    global obj
    if cv2.contourArea(c) < 2000:             #过滤掉较面积小的物体
      
      continue
    else:
      target_list.append(c)
                     #将面积较大的物体视为目标并存入目标列表
  for i in target_list:                       #绘制目标外接矩形
    rect = cv2.minAreaRect(i)
    box = cv2.boxPoints(rect)
    cv2.drawContours(draw_img, [np.int0(box)], -1, (0, 255, 255), 2)
  
  return draw_img

#定义一个绘制中心点坐标的函数
def draw_center(target_list,draw_img):
    center_x = 0
    center_y = 0
    if (True == True):
        for c in target_list:
            M = cv2.moments(c)                   #计算中心点的x、y坐标
            center_x = int(M['m10']/M['m00'])
            center_y = int(M['m01']/M['m00'])
        #print('center_x:',center_x)
        #print('center_y:',center_y)
        cv2.circle(draw_img,(center_x,center_y),7,128,-1)#绘制中心点
        str1 = '(' + str(center_x)+ ',' +str(center_y) +')' #把坐标转化为字符串
        cv2.putText(draw_img,str1,(center_x-50,center_y+40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)#绘制坐标点位
    
    
    return draw_img



count = 0
t = 0
x = 0
y = 0

flag = 0  
flag_body = 0

x11d = 0
x11d = 0
x12d = 0
x13d = 0
x21d = 0
x22d = 0
x23d = 0
x31d = 0
x32d = 0
x33d = 0

y11d = 0
y12d = 0
y13d = 0
y21d = 0
y22d = 0
y23d = 0
y31d = 0
y32d = 0
y33d = 0

class FaceDetection(Node):
  """
  Create an FaceDetection class, which is a subclass of the Node class.
  """
  def __init__(self):
    """
    Class constructor to set up the node
    """
    # Initiate the Node class's constructor and give it a name
    super().__init__('face_detection')
      
    # Create the subscriber. This subscriber will receive an Image
    # from the video_frames topic. The queue size is 10 messages.
    self.subscription = self.create_subscription(
      Image, 
      '/image_raw',
      self.listener_callback, 
	  	qos_profile_sensor_data)
    self.subscription # prevent unused variable warning

    # Used to convert between ROS and OpenCV images
    self.br = CvBridge()
   
   
  #定义一个形态学处理的函数

  def listener_callback(self, data):
    """
    Callback function.
    """
    # Display the message on the console
    global target_list11
    target_list11 = []
    global target_list12
    target_list12 = []
    global target_list13
    target_list13 = []
    global target_list21
    target_list21 = []
    global target_list22
    target_list22 = []
    global target_list23
    target_list23 = []
    global target_list31
    target_list31 = []
    global target_list32
    target_list32 = []
    global target_list33
    target_list33 = []
    
    

   
    self.get_logger().info('Receiving image')
 
    # Convert ROS Image message to OpenCV image
    current_frame = self.br.imgmsg_to_cv2(data, "bgr8")
    #return current_frame
    arm_init()
    #img = 0
    img = current_frame
    
    img = img[0:680,250:600]
    first_img = img [370:500,0:480]
    second_img = img [170:360,0:480]
    third_img = img [0:160,0:480]
    
    
    draw_img = img 
    erode_hsv = good_thresh_img(img)
    final_inRange_hsv = select_color_img(target_color,erode_hsv)
    contours = extract_contour(final_inRange_hsv)
    #draw_img1 = count_timer(draw_img)
    draw_img = find_target(contours,draw_img)
    final_img = draw_center(target_list,draw_img)
 
        #fisrt - color select
    erode_hsv1 = good_thresh_img(first_img)
    final_inRange_blue1 = select_color_blue(target_color2,erode_hsv1)
    final_inRange_red1 = select_color_red(target_color3,erode_hsv1)
    final_inRange_green1 = select_color_green(target_color1,erode_hsv1)
    #final_inRange_yellow1 = select_color_yellow(target_color4,erode_hsv1) 
    
    
    #second - color select
    erode_hsv2 = good_thresh_img(second_img)
    final_inRange_blue2 = select_color_blue(target_color2,erode_hsv2)
    final_inRange_red2 = select_color_red(target_color3,erode_hsv2)
    final_inRange_green2 = select_color_green(target_color1,erode_hsv2)
    #final_inRange_yellow1 = select_color_yellow(target_color4,erode_hsv1)
    
    #third  - color select
    erode_hsv3 = good_thresh_img(third_img)
    final_inRange_blue3 = select_color_blue(target_color2,erode_hsv3)
    final_inRange_red3 = select_color_red(target_color3,erode_hsv3)
    final_inRange_green3 = select_color_green(target_color1,erode_hsv3)
    
    
    #first - center
    contours_blue1 = extract_contour(final_inRange_blue1)
    contours_red1 = extract_contour(final_inRange_red1)
    contours_green1 = extract_contour(final_inRange_green1)
    #contours_yellow1 = extract_contour(final_inRange_yellow1)
    
    draw_img_blue1 = find_target11(contours_blue1,first_img)
    draw_img_red1 = find_target12(contours_red1,first_img)
    draw_img_green1 = find_target13(contours_green1,first_img)
    #draw_img_yellow1 = find_target(contours,first_img)
    final_img_blue1,x11,y11 = draw_center11(target_list11,draw_img_blue1)
    final_img_red1,x12,y12 = draw_center12(target_list12,draw_img_red1)
    final_img_green1,x13,y13 = draw_center13(target_list13,draw_img_green1)
    
    
    #second - center
    contours_blue2 = extract_contour(final_inRange_blue2)
    contours_red2 = extract_contour(final_inRange_red2)
    contours_green2 = extract_contour(final_inRange_green2)
    #contours_yellow1 = extract_contour(final_inRange_yellow1)
    
    draw_img_blue2 = find_target21(contours_blue2,second_img)
    draw_img_red2 = find_target22(contours_red2,second_img)
    draw_img_green2 = find_target23(contours_green2,second_img)
    #draw_img_yellow1 = find_target(contours,first_img)
    final_img_blue2,x21,y21 = draw_center21(target_list21,draw_img_blue2)
    final_img_red2,x22,y22 = draw_center22(target_list22,draw_img_red2)
    final_img_green2,x23,y23 = draw_center23(target_list23,draw_img_green2)
    
    
    #third - center
    contours_blue3 = extract_contour(final_inRange_blue3)
    contours_red3 = extract_contour(final_inRange_red3)
    contours_green3 = extract_contour(final_inRange_green3)
    #contours_yellow1 = extract_contour(final_inRange_yellow1)
    
    draw_img_blue3 = find_target31(contours_blue3,third_img)
    draw_img_red3 = find_target32(contours_red3,third_img)
    draw_img_green3 = find_target33(contours_green3,third_img)
    #draw_img_yellow1 = find_target(contours,first_img)
    final_img_blue3,x31,y31 = draw_center31(target_list31,draw_img_blue3)
    final_img_red3,x32,y32 = draw_center32(target_list32,draw_img_red3)
    final_img_green3,x33,y33 = draw_center33(target_list33,draw_img_green3)
    #x,y = focus_center(target_list,draw_img1)
    #flag = 0
 
    t = 0
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    

    flag = 0
    flag_body = 0
 
    global count 
    count = count + 1
    
    #time.sleep(3)

    #if(count == 3):
   #   x2 = x
   #   y2 = y
   #   flag = 1
   #   #global count
    #  count = 0
    #  print("flag")
    #else:
     # x2 = x2
     # y2 = y2
     # flag = 0
      
    if(count == 1):
      x11d = x11
      y11d = y11
      x12d = x12
      y12d = y12
      x13d = x13
      y13d = y13
      x21d = x21
      y21d = y21
      x22d = x22
      y22d = y22
      x23d = x23
      y23d = y23
      x31d = x31
      y31d = y31
      x32d = x32
      y32d = y32
      x33d = x33
      y33d = y33
        
        
      flag = 1
      count = 0
      print("ok")
    else:
      x11d = x11d
      y11d = y11d
      x12d = x12d
      y12d = y12d
      x13d = x13d
      y13d = y13d
      x21d = x21d
      y21d = y21d
      x22d = x22d
      y22d = y22d
      x23d = x23d
      y23d = y23d
      x31d = x31d
      y31d = y31d
      x32d = x32d
      y32d = y32d
      x33d = x33d
      y33d = y33d
      flag = 0
      print(count)
       
        
    #x2,y2,flag = count_timer(x,y,flag) 
    #x2,y2 = focus_center2(target_list,draw_img)
     
    if (((x11d > 50) and (x11d < 250)) and ((y11d > 15) and (y11d < 100)) and (flag == 1)):
      arm_first_body_catch()
      arm_first_body_init()
      arm_third_body_down()
      arm_third_init()
       #target_list =[]
      print("blue_3_finish")
    if (((x12d > 50) and (x12d < 250)) and ((y12d > 15) and (y12d < 100)) and (flag == 1)):
      arm_first_body_catch()
      arm_first_body_init()
      arm_first_body_down()
      arm_init()
       #target_list =[]
      print("red_1_finish")
    if (((x13d > 50) and (x13d < 250)) and ((y13d > 5) and (y13d < 100)) and (flag == 1)):
      arm_first_body_catch()
      arm_first_body_init()
      arm_second_body_down()
      arm_second_init2()
      #target_list =[]
      print("green_2_finish")
        
    if (((x21d > 50) and (x21d < 250)) and ((y21d > 5) and (y21d < 100)) and (flag == 1)):
      arm_second_catch()
      arm_second_body()
      arm_third_body_down()
      arm_third_init()
       #target_list =[]
      print("blue_3_finish")
    if (((x22d > 50) and (x22d < 250)) and ((y22d > 5) and (y22d < 100)) and (flag == 1)):
      arm_second_catch()
      arm_second_body()
      arm_first_body_down()
      arm_init()
       #target_list =[]
      print("red_1_finish")    
    if (((x23d > 50) and (x23d < 250)) and ((y23d > 5) and (y23d < 100)) and (flag == 1)):
      arm_second_catch()
      arm_second_body()
      arm_second_body_down()
      arm_second_init2()
       #target_list =[]
      print("green_2_finish")
    
    if (((x31d > 50) and (x31d < 250)) and ((y31d > 5) and (y31d < 100)) and (flag == 1)):
      arm_third_body_catch()
      arm_third_body_init()
      arm_third_body_down()
      arm_third_init()
       #target_list =[]
      print("blue_3_finish")
    if (((x32d > 50) and (x32d < 250)) and ((y32d > 5) and (y32d < 100)) and (flag == 1)):
      arm_third_body_catch()
      arm_third_body_init()
      arm_first_body_down()
      arm_init()
       #target_list =[]
      print("red_1_finish")    
    if (((x33d > 50) and (x33d < 250)) and ((y33d > 5) and (y33d < 100)) and (flag == 1)):
      arm_third_body_catch()
      arm_third_body_init()
      arm_second_body_down()
      arm_second_init2()
       #target_list =[]
      print("green_2_finish")   
    #else:
      #cv2.imshow('final_img',final_img)
    #break
    #arm_first_body_catch()
    
    #break
    # Display image
    #cv2.imshow('final_img',final_img)
    


    
    #cv2.waitKey(1) 
    
    #return current_frame


  
def main(args=None):
  
  # Initialize the rclpy library
  rclpy.init(args=args)
  
  # Create the node
  face_detection = FaceDetection()
  
  # Spin the node so the callback function is called.
  rclpy.spin(face_detection)
  
  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)

  
    
    
  # Shutdown the ROS client library for Python
  face_detection.destroy_node()
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()
