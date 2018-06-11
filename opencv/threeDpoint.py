
import SIFT
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import HarrisCorner
import cv2



def get3d(img1,img2):
	data = SIFT.sift(img1,img2)

	#cv2.triangulatePoints(projMatr1, projMatr2, data[0], data[1])




	x = []
	y = []
	z = []
	for i in range(0,len(data[0])):
		x.append(data[0][i][0])
		y.append(data[0][i][1])
		if (abs(data[0][i][1]-data[1][i][1])*abs(data[0][i][1]-data[1][i][1])+abs(data[0][i][0]-data[1][i][0])*abs(data[0][i][0]-data[1][i][0]))/2 > 300:
			z.append(0)
		else:
			z.append((abs(data[0][i][1]-data[1][i][1])*abs(data[0][i][1]-data[1][i][1])+abs(data[0][i][0]-data[1][i][0])*abs(data[0][i][0]-data[1][i][0]))/2)
		



	fig = plt.figure()
	'''ax = fig.add_subplot(111, projection='3d')





	ax.scatter(x, y, z, c='r', marker='o')

	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')

	plt.show()'''
	return zip(x,y,z)
