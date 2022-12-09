# KR260配置生成Linux内核

## 目的：使用Pl端的外设IO，需要通过Vivado配置.xsa文件，重新生成PS端的Linux Kernel

## Table of Contents

- [0. Environment](#0-Environment)

- [1. 软件安装](#1-软件安装-仅针对vivado中添加kr260-kit)
- [2. Petalinux 的生成过程](#2-petalinux-的生成过程-linux)
  - [2.1 下载Petalinux](#21-下载petalinux)
  - [2.2 安装前的环境配置](#22-安装前的环境配置)
     - [2.2.1 配下载需要的依赖环境置源](#221-下载需要的依赖环境)
     - [2.2.2 安装tftp服务](#222-安装tftp服务)
     - [2.2.3 更换dash](#223-更换dash)
  - [2.3 安装Petalinux](#23-安装petalinux)
  - [2.4 s下载KR260的bsp文件](#24-下载kr260的bsp文件)
- [3. 工程文件的配置](#3-工程文件的配置)
  - [3.1 实现设计](#31-实现设计)
  - [3.2 导出硬件描述文件](#32-导出-硬件描述-文件)
- [4. Petalinux 生成内核](#4-petalinux-生成内核)
  - [4.1 生成需要的内核文件](#41-生成需要的内核文件)
  - [4.2 对用户设备树文件添加声明](#42-对用户设备树文件添加声明)
  - [4.3 生成启动文件](#43-生成启动文件)
- [5. 配置sd卡](#5-配置sd卡)
  - [5.1 烧写sd卡](#51-烧写sd卡)
  - [5.2 对SD卡解除挂载](#52-对sd卡解除挂载)
- [6. 更新BOOT.BIN固件](#6-更新bootbin固件)

 

## 0. Environment
软件版本：vivado 2022.1，PetaLinux 2022.1 （强制，否则无法成功）

操作系统：Ubuntu Linux 20.04 

KR260相关：xilinx_kr260.bsp，Ubuntu 22.04 LTS

## 1. 软件安装 (仅针对Vivado中添加KR260 Kit)

  进入Vivado的界面，在左上角选择Tool-->Vivado Store 进入

![here](https://github.com/shilicon/kr260/blob/main/image/vivado.JPEG)

1. Go to git

在Vivado Store里，如果是外网，可以直接利用Refresh更新，获得KR260的支持包。Vivado全局科学上网 也更新不了，选择Go to Git。
![here](https://github.com/shilicon/kr260/blob/main/image/vivadoStore.jpeg)

2. 在网站中选择board，查看支持的板卡
![here](https://github.com/shilicon/kr260/blob/main/image/vivadoGit.JPEG)


3. 能够看到支持的板卡 vendor，是可以发现，一家Xilinx的官方板卡都没有。（这个问题让我困惑了很久）。选择master，查看Branches，可以发现针对2022.1的版本，里面有针对KR260的。

![here](https://github.com/shilicon/kr260/blob/main/image/vivadoBoard.jpeg)

![here](https://github.com/shilicon/kr260/blob/main/image/vivadoBra1.jpeg)
![here](https://github.com/shilicon/kr260/blob/main/image/vivadoBra2.jpeg)

4.  git clone 这个库，并且更新分支和本地代码。以下是KR260的支持文件
```
git clone https://github.com/Xilinx/XilinxBoardStore
git branch 2022.1
git pull

```

5. 把文件放到Vivado的路径下。（在Windows里，这个文件路径在软件安装路径下）
```
D:\vivado\Vivado\2022.1\data\xhub\boards\XilinxBoardStore\boards\Xilinx
```
将文件解压后导入文件夹，然后重启vivado，就能在新建工程时的板卡选取看到
![here](https://github.com/shilicon/kr260/blob/main/image/vivadoStore2.jpeg)

## 2. Petalinux 的生成过程 (Linux)
### 2.1 下载Petalinux 

通过 Xilinx 官网下载：
See [Here](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/embedded-design-tools/archive.html)

需要下载2022.1的版本，只有版本才支持KR260。
### 2.2 安装前的环境配置
#### 2.2.1 下载需要的依赖环境

在Terminal中执行以下指令
```
sudo apt-get install build-essential vim tofrodos \
iproute2 gawk gcc git make net-tools zlib1g-dev \
libssl-dev flex bison libselinux1 libncurses5-dev \
tftpd lib32z1 lib32ncurses5-dev libbz2-1.0:i386 \
lib32stdc++6 xvfb chrpath socat autoconf libtool

sudo apt-get install texinfo gcc-multilib libsdl1.2-dev \
libglib2.0-dev zlib1g:i386 libncurses5 libncurses5-dev \
libc6:i386 libstdc++6:i386 zlib1g:i386 libssl-dev tftpd \
tftp openbsd-inetd xterm
```

#### 2.2.2 安装tftp服务
输入以下指令
```
sudo apt-get install tftpd tftp openbsd-inetd
sudo gedit /etc/inetd.conf
```
在打开的文件最后一行加入  
```
  tftp dgram udp wait nobody /usr/sbin/tcpd /usr/sbin/in.tftpd /tftproot
``
保存后退出，之后在Terminal中输入如下命令
```
  sudo mkdir /tftproot
  sudo chmod 777 /tftproot
  /etc/init.d/openbsd-inetd restart
``
输入netstat -an | more | grep udp命令，打印出udp 0 0 0.0.0.0:69 0.0.0.0:* 即为安装成功

#### 2.2.3 更换dash
petalinux的/bin/sh命令需要使用bash，而Ubuntu默认的/bin/sh命令是dash的，所以需要进行更换
输入以下指令,在出现的界面中选择‘否’：
```
dpkg-reconfigure dash
```
### 2.3 安装Petalinux
  将第一步下载好的安装文件放入工作路径，新建文件夹 mkdir petalinux，在工作路径下打开Terminal命令：
```
chmod 777 ./petalinux-v2020.2-final-installer.run
./petalinux-v2020.2-final-installer.run -d ./petalinux
```
安装过程中需要同意三个许可，回车阅读许可，按q返回，输入y同意许可

  验证是否安装成功，Terminal中输入 source /workpath/petalinux/settings.sh

  Terminal中输入echo $PETALINUX

  如果打印出正确的安装路径说明安装成功，如：
  ![here](https://github.com/shilicon/kr260/blob/main/image/petalinux.png)

  ### 2.4 下载KR260的bsp文件
 See [Here](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+K26+SOM)
 ![here](https://github.com/shilicon/kr260/blob/main/image/bsp.jpeg)

 以下两个warning不需要解决，不影响正常使用
   ![here](https://github.com/shilicon/kr260/blob/main/image/warning.jpeg)

 ## 3. 工程文件的配置
 ### 3.1 实现设计
 略，根据自己的需求，完成编译和综合

 ### 3.2 导出 硬件描述 文件
 生成bit流文件，点击 File -> Export -> Export Hardware
   ![here](hardware.png)
 ## 4. Petalinux 生成内核
 ### 4.1 生成需要的内核文件

在Terminal中执行以下命令
 ```
petalinux-create -t project -s xilinx-kr260-starterkit-v2022.1-05140151.bsp
cd xilinx-kr260-starterkit-2022.1
petalinux-config --silentconfig --get-hw-description *.xsa
petalinux-build
//这一步大概需要30～40分钟
 
 ```

 ### 4.2 对用户设备树文件添加声明
 在“~/Petalinux/xilinx-kr260-starterkit-2022.1/components/plnx_workspace/device-tree/device-tree”路径下，找到pcw.dtsi，添加以下字段
 ```
&axi_iic_0 {

              status = "okay";

};
 ```
 之后重新编译设备树
 ```
petalinux-build -c device-tree -x cleansstate
petalinux-build -c device-dree
 ```

 ### 4.3 生成启动文件
```
petalinux-package --boot --u-boot --fsbl --fpga --force
petalinux-package --wic --images-dir images/linux/ --bootfiles "ramdisk.cpio.gz.u-boot,boot.scr,Image,system.dtb,system-zynqmp-sck-kr-g-revB.dtb" /dev/sda
 //这两步不能在root下执行指令，因为没有配置root的路径，导致一执行就会出错
```

## 5. 配置SD卡
### 5.1 烧写SD卡
```
 sudo dd if=petalinux-sdimage.wic of=/dev/sda conv=fsync
```

### 5.2 对SD卡解除挂载
```
sudo eject /dev/sda
```
## 6. 更新BOOT.BIN固件

Xilinx针对KR260和KV260设计了一种更先进的固件更新方法，可以在Ubuntu中使用 “xmutil bootfw_update”进行底层的固件更新。

KR260的固件是烧写在flash当中的，所以必须要更新flash固件，才可以看到更新后的设备树。

将BOOT.BIN 放入根目录，在Ubuntu下打开Terminal，输入以下指令
```
xmutil bootfw_update -i ./BOOT.BIN
// 重新物理上电
xmutil bootfw_update -v
```
此时能够查看到已经更新的固件

 
