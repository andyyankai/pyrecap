
import SIFT
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

data = SIFT.sift()

x = []
y = []
z = []
for i in data:
	x.append(i[0])
	y.append(i[1])
	z.append(i[2])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')





ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
