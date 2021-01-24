#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32MultiArray
from object_detector import ObjectDetector

def lidar_callback(self, msg):
#   msg.ranges #常時360個の配列となる
#   msg.angle_min # スキャンの開始角度[rad] 常時約-3.14radとなる
#   msg.angle_max # スキャンの終了角度[rad] 常時約3.14radとなる
#   msg.angle_increment # 計測間隔[rad] 常時0.017rad = 1degreeとなる
#   msg.range_min # 最小検出距離[m] 常時約0.15mとなる
#   msg.range_max # 最大検出距離[m] 常時約12.00mとなる
    objdtct = ObjectDetector()
    dist_list = objdtct.GetObject2D(msg.ranges)
    pub.publish(dist_list)


if __name__ == '__main__':
  
  rospy.init_node('drive_mod')
  rospy.Subscriber("rplidar_scan", LaserScan, lidar_callback) 
  # 1: name of the Topic, 2: data type of the topic 3: callback func
  pub = rospy.Publisher('ptop_distnce', Float32MultiArray, queue_size = 1)

  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    rate.sleep()