import rospy
import geometry_msgs
from geometry_msgs.msg import PoseStamped
import time
import numpy as np
import scipy.optimize as optimization
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

track_list = []
list_x = []
list_y = []
list_z = []
track_time = []
TRACK_REC_INTERVAL = .15 # seconds 
last_call = 0
iterator = 1
ax = plt.axes(projection = "3d")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

def trajectory():
	global iterator
	if(len(list_x) == 0):
		return
	x = np.array(list_x)
	y = np.array(list_y)
	z = np.array(list_z)
	trendxy = np.polyfit(x, y, deg = 2)
	trendxz = np.polyfit(x, z, deg = 2)
	f1 = np.poly1d(trendxz)
	f = np.poly1d(trendxy)
	x_new = np.linspace(x[0], 15, 500)
	ys = []
	zs = []
	for i in range(len(x_new)):
		ys.append(f(x_new[i]))
		zs.append(f1(x_new[i]))
	if(iterator >= 7 and iterator <= 10):
		ax.plot3D(x_new, ys, zs, label = str(iterator))

	iterator+= 1

def pose_callback(pose_msg):
	global list_x, list_y, list_z
	temp = [pose_msg.pose.position.x,pose_msg.pose.position.y,pose_msg.pose.position.z]
	list_x.append(float(temp[0]))
	list_y.append(float(temp[1]))
	list_z.append(float(temp[2]))
	track_list.append(temp)
	track_time.append(pose_msg.header.stamp)

def main():

	global track_time, track_list, last_call, list_x, list_y
	rospy.init_node("Tracker")
	tracker_sub = rospy.Subscriber("/vrpn_client_node/radarmount/pose", PoseStamped, pose_callback)
	# rospy.spin()
	last_call = 0
	start_time = time.time()
	while not rospy.is_shutdown():
		if time.time() - last_call > TRACK_REC_INTERVAL:
			last_call = time.time()
			# print(last_call)
			trajectory()
			# print(track_list[-1:])
	print("TOTAL ITERATIONS: " + str(iterator))
	plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
	plt.show()
if __name__=="__main__":
	main()
