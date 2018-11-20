import numpy as np
import scipy.optimize as optimization
import matplotlib.pyplot as plt

def func(x,a,b,c):
	return a + b *x + c * x**2

def main():
	mocap_x = np.array([0,0.86,1.72,2.58])
	mocap_y = np.array([0,1.18,2.26,3.24])
	x_0 = np.array([0,0,0])
	sigma = np.array([1.0] * len(mocap_x))
	abc, covar = optimization.curve_fit(func,mocap_x, mocap_y, x_0, sigma)
	print(abc)
	x = []
	y = []
	i = 0
	while(func(i,abc[0],abc[1],abc[2]) >= 0):
		x.append(i)
		y.append(func(i,abc[0],abc[1],abc[2]))
		i += .05
	plt.plot(x,y)
	plt.xlim(0, 23)
	plt.ylim(0, 8)
	plt.show()

if __name__ == '__main__':
	main()