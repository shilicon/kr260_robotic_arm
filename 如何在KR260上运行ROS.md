# 如何在KR260上运行ROS

## 什么是ROS？
机器人操作系统（ROS）是一套软件库和工具，可以帮助你建立机器人应用。从驱动程序到最先进的算法，以及强大的开发者工具，ROS拥有你的下一个机器人项目所需要的东西。而且都是开源的。

ROS虽然叫做机器人操作系统，但本质并不是操作系统，而是一个软件工具。它的作用是抽象机器人控制和传感器驱动的过程，让不同协议的器件之间能够互相通信。起到了一个总线的作用，不需要交互协议，所有的控制用Python，C++完成即可

## Table of Contents

- [0. Environment](#0-Environment)

- [1. Installation ROSs](#1-Installation-ROS)
- [2. Steps](#2-steps)
  - [2.1 安装依赖](#21-安装依赖)
  - [2.2 保证UTF-8的支持](#22-保证UTF-8的支持)
  - [2.3 配置源](#23-配置源)
  - [2.4 下载ROS2包](#24-下载ros2包)
  - [2.5 source ROS 到环境中](#25-source-ros-到环境中)
  - [2.6 测试安装成功](#26-测试安装成功)
- [3. 机械臂工程配置部分](#3-机械臂工程配置部分)
 

  ## 0. Environment
  1. Hardware: KR260
  2. OS: Ubuntu 22.04 (运行在KR260，目前仅支持该版本)
  3. ROS：ROS2 Humble （Ubuntu 22 目前仅支持该版本）

  ## 1. Installation ROS
  https://docs.ros.org/en/humble/Installation.html

  ## 2. Steps (在KR260的Ubuntu中)
  ### 2.1 安装依赖
  ```
  locale  # check for UTF-8
  sudo apt-get update
  sudo apt-get install curl gnupg2 lsb-release vim  
  sudo apt update && sudo apt install locales
  sudo apt-get install g++
  sudo apt install python3-colcon-common-extensions   
  sudo apt-get -y install curl build-essential libssl-dev git wget ocl-icd-* opencl-headers python3-vcstool  python3-colcon-mixin kpartx u-boot-tools pv libgazebo11-dev
  sudo apt-get install -y build-essential cmake make pkg-config
  sudo apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
  sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev
  sudo apt-get install -y libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev
  sudo apt-get install -y libatlas-base-dev gfortran
  sudo apt-get install -y python3-dev
  ```
  ### 2.2 保证UTF-8的支持
  ```
  sudo apt-get install -y python3-dev
  sudo locale-gen en_US en_US.UTF-8
  sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
  export LANG=en_US.UTF-8
  locale  # verify settings
  ```

  ### 2.3 配置源
  ```
  apt-cache policy | grep universe
  sudo apt install software-properties-common
  sudo add-apt-repository universe
  sudo apt update && sudo apt install curl gnupg lsb-release
  sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg   
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

  curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
  sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
  ```

  ### 2.4 下载ROS2包

  下载的内容之前已经配置好了，因此这里只需要更新一下，直接下载就可以了。
  
  ```
  sudo apt update
  sudo apt upgrade
  sudo apt install ros-humble-desktop
  sudo apt install ros-humble-ros-base
  ```

  ### 2.5 source ROS 到环境中

  ```
  source /opt/ros/humble/setup.bash
  ```

  ### 2.6 测试安装成功
  分别打开两个Terminal，输入以下指令，第一个部分为发送数据，第二个部分为接收数据
  ```
  . ~/ros2_humble/install/local_setup.bash
  ros2 run demo_nodes_cpp talker
  ```

  ```
  . ~/ros2_humble/install/local_setup.bash
  ros2 run demo_nodes_py listener
  ```
  期待的结果：左，发布信息；右，接收信息
 ![here](https://github.com/shilicon/kr260_robotic_arm/blob/main/talk_sub.png)
