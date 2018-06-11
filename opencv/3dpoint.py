
import SIFT
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import HarrisCorner

data = SIFT.sift()

cv2.triangulatePoints(projMatr1, projMatr2, data[0], data[1])




'''x = []
y = []
z = []
for i in data[1]:
	x.append(i[0])
	y.append(i[1])
	z.append(0)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')





ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()'''
