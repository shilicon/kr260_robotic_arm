# opencv_ros2
OpenCV Applications with ROS2

Environment
* Ubuntu 20.04
* ROS2 Foxy
* OpenCV 4.2.0
  * pip install opencv-python
  * pip install numpy
* Python 3.8.10
* vision_opencv - https://github.com/ros-perception/vision_opencv/tree/ros2

Applications
* sub
* take_photo
* face_detection
* camshift
* qrcode_detector

Camera

Webcam
* ros2 run usb_cam usb_cam_node_exe
* /image_raw
* ros2 launch usb_cam demo_launch.py
* ros2 run rqt_image_view rqt_image_view

Orbbec Astra
* ros2 run astra_camera astra_camera_node
* /image /depth
* ros2 run image_tools showimage --ros-args --remap image:=/image -p reliability:=best_effort

Execution
* ros2 run opencv_ros2 face_detection
