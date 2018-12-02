import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
import cv2
import cv_bridge
import dlib
import time

FLIGHT_TIME = 45 # seconds



def main():
  rospy.init_node("Initialize")
  takeoff_pub = rospy.Publisher.
  # take off
  takeoff_pub.publish(Empty())
  sleep 4 seconds

  while not rospy.is_shutdown() and time.time() - start_time < FLIGHT_TIME:
      pos_update = Twist()
      collision = false
      moved = false
      move_dist = .15
      # get position of quadcopter from mocap
      quad_x = 0
      quad_y = 0
      quad_z = 0
      # get list of lists for points over time of thrown object
      movement = [[],[],[]]

      # calculate all the points in the path
      for point in range(0,len(movement), 10):
          if (abs(quad_x-movement[point][0]) < 15 and abs(quad_y-movement[point][1]) < 15 and abs(quad_z-movement[point][2]) < 15)
            collision = true
      # if point is within buffer, move
      if collision == true:
          pos_update.linear.x = move_dist
          moved = true  # will this execute after the movement or right away?
          drone_pub.publish(pos_update)
      rospy pause.........
      # return to original position.... will this execute before the quadcopter has moved?
      if moved == true:
          pos_update.linear.x =  -move_dist

  # land after flight time reached
  landing_pub.publish(Empty())
  print("Shutdown")

if __name__ == '__main__':
    bridge = cv_bridge.CvBridge()
    main()
