# 基于KR260的机械臂控制器设计
这是一个在AMD/Xilinx Kria KR260 FPGA板卡上实现机械臂抓取物体的工程，目前提供的文件有：

- 可实现机械臂功能的ROS文件,功能：图像实时显示，红绿蓝颜色识别，机械臂定点物体抓取，分类放置。
- 启动KR260的教程文档
- 在KR260 Ubuntu上安装ROS的教程文档
- 使用PL+PS端的Linux image文档 (与工程无关，提供参考开发)

## Table of Contents

- [0. Environment](#0-Environment)

- [1. 使用流程](#1-使用流程)
  - [1.1 KR260 启动](#11-kr260-启动)
  - [1.2 KR260 ROS环境配置](#12-kr260-ros环境配置)
    - [1.2.1 ROS2](#121-ros2)
    - [1.2.2 Camera](#122-camera)
- [2. 机械臂工程配置](#2-机械臂工程配置)
  - [2.1 设计参考](#21-设计参考)
  - [2.2 主要步骤](#22-主要步骤)

## 0. Environment

本项目使用AMD/Xilinx的Kria KR260 FPGA开发套件

关于KR260的官方介绍在[这里](https://china.xilinx.com/products/som/kria/kr260-robotics-starter-kit.html)

本项目在以下环境中完成测试：
- Ubuntu版本：Ubuntu 22.0
- ROS2版本：ROS2 Humble
- 编程语言：Python 3.10
- 机械臂类型：STM32驱动6自由度PWM机械臂
- 机械臂通信方式：USB 串口通信
- 摄像头：免驱USB摄像头

摄像头识别的部分，使用了OpenCV框架：
- [opencv_ros2](https://github.com/jeffreyttc/opencv_ros2)
- [vision_opencv](https://github.com/ros-perception/vision_opencv/tree/ros2)
 
## 1. 使用流程：

### 1.1 KR260 启动
See [如何启动KR260](https://github.com/shilicon/kr260_robotic_arm/blob/main/%E5%A6%82%E4%BD%95%E5%90%AF%E5%8A%A8KR260.md)

### 1.2 KR260 ROS环境配置
#### 1.2.1 ROS2
See [在KR260上运行ROS](https://github.com/shilicon/kr260_robotic_arm/blob/main/%E5%A6%82%E4%BD%95%E5%9C%A8KR260%E4%B8%8A%E8%BF%90%E8%A1%8CROS.md)

#### 1.2.2 Camera
```
sudo apt install ros-humble-usb-cam
```

## 2. 机械臂工程配置

### 2.1 设计参考 
See [opencv_ros2](https://github.com/jeffreyttc/opencv_ros2)

and

See [vision_opencv](https://github.com/ros-perception/vision_opencv/tree/ros2)

### 2.2 主要步骤:
#### 2.2.0. 下载工程文件

使用以下指令下载ROS2的文件

```
git clone https://github.com/shilicon/kr260_robotic_arm
```
文件结构如下：

```
├── opencv_ros2
│   ├── opencv_ros2
│   ├── resource
│   └── test
└── vision_opencv
    ├── cv_bridge
    │   ├── cmake
    │   ├── doc
    │   ├── include
    │   │   └── cv_bridge
    │   ├── python
    │   │   └── cv_bridge
    │   ├── src
    │   └── test
    ├── image_geometry
    │   ├── doc
    │   ├── image_geometry
    │   ├── include
    │   │   └── image_geometry
    │   ├── src
    │   └── test
    ├── opencv_tests
    │   ├── launch
    │   ├── opencv_tests
    │   └── resource
    └── vision_opencv

```
#### 2.2.1. 工作空间的编译

*编译机械臂的工程
```
cd kr260
colcon build
```

#### 2.2.2. open camera (new terminal） 
```
ros2 run usb_cam usb_cam
```

#### 2.2.3. show image (new terminal)

*显示摄像头采集到的彩色数据
```
cd kr260
source install/setup.bash
ros2 run opencv_ros2 sub
```
#### 2.2.4. show color detection (new terminal)

*显示识别区域颜色识别后的结果(hsv)
```
cd kr260
source install/setup.bash
ros2 run opencv_ros2 video_subscriber
```
#### 2.2.5. Robotic Arm (new terminal)

*机械臂会根据摄像头的颜色识别结果，抓取物体，并按颜色分类放置

*此处的指令名称来自参考的设计，其本身是人脸识别，进一步修改时保留了这个名字
```
cd kr260
source install/setup.bash
ros2 run opencv_ros2 face_detection
```





