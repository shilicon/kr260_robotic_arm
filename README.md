# kr260
这是一个在KR260上实现机械臂抓取物体的工程
## Table of Contents

- [0. Environment](#0-Environment)

- [1. Applications](#1-Applications)
- [2. 使用流程](#2-使用流程)
  - [2.1 KR260 启动部分](#21-KR260-启动部分)
  - [2.2 KR260 ROS环境配置部分](#22-KR260-ROS环境配置部分)
    - [2.2.1 ROS2](#221-ROS2)
    - [2.2.2 Camera](#222-Camera)
- [3. 机械臂工程配置部分](#3-机械臂工程配置部分)
  - [3.1 设计参考](#31-设计参考)
  - [3.2 Step](#32-step)
## 0. Environment
Ubuntu版本：Ubuntu 22.0

ROS2版本：ROS2 Humble

编程语言：Python 3.10

机械臂类型：STM32驱动6自由度PWM机械臂

机械臂通信方式：USB 串口通信

摄像头：免驱USB摄像头

[opencv_ros2](https://github.com/jeffreyttc/opencv_ros2)

[vision_opencv](https://github.com/ros-perception/vision_opencv/tree/ros2)

# 1. Applications
*实时图像显示

*红绿蓝颜色识别

*机械臂定点抓取物体，对颜色物体进行分类放置
 
# 2. 使用流程：

## 2.1 KR260 启动部分
See [如何启动KR260](https://thzn1lcm0h.feishu.cn/docx/doxcn2yrBMQl4JnLwFVXuW3C4LN)

## 2.2 KR260 ROS环境配置部分
### 2.2.1 ROS2
See [在KR260上运行ROS](https://thzn1lcm0h.feishu.cn/docx/doxcnyfMwmHVpES1tX9Ex9bRfkb)

### 2.2.2 Camera
```
sudo apt install ros-humble-usb-cam
```

## 3. 机械臂工程配置部分

### 3.1 设计参考 
See [opencv_ros2](https://github.com/jeffreyttc/opencv_ros2)

and

See [vision_opencv](https://github.com/ros-perception/vision_opencv/tree/ros2)

### 3.2 Step:
1. 工作空间的编译

*编译机械臂的工程
```
cd kr260
colcon build
```

2. open camera (new terminal） 
```
ros2 run usb_cam usb_cam
```

3. show image (new terminal)

*显示摄像头采集到的彩色数据
```
cd kr260
source install/setup.bash
ros2 run opencv_ros2 sub
```
4. show color detection (new terminal)

*显示识别区域颜色识别后的结果(hsv)
```
cd kr260
source install/setup.bash
ros2 run opencv_ros2 video_subscriber
```
5. Robotic Arm (new terminal)

*机械臂会根据摄像头的颜色识别结果，抓取物体，并按颜色分类放置

*此处的指令名称来自参考的设计，其本身是人脸识别，进一步修改时保留了这个名字
```
cd kr260
source install/setup.bash
ros2 run opencv_ros2 face_detection
```





