from setuptools import setup

package_name = 'opencv_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jupiter',
    maintainer_email='jupiter@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'img_publisher = opencv_ros2.webcam_pub:main',
          'img_subscriber = opencv_ros2.webcam_sub:main',
          'face_detection = opencv_ros2.face_detection:main',
          'camshift = opencv_ros2.camshift:main',
          'camshift_tracker = opencv_ros2.camshift_tracker:main',
          'qrcode_detector = opencv_ros2.qrcode_detector:main',
          'take_photo = opencv_ros2.take_photo:main',
          'video_subscriber = opencv_ros2.video_subscriber:main',
          'canny_edge_detection = opencv_ros2.canny_edge_detection:main',
          'sub = opencv_ros2.sub:main',
        ],
    },
)
