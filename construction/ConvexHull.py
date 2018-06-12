
'''dataarray = objectmaker.run()
print(len(dataarray))
a = [i[0] for i in dataarray]
b = [i[1] for i in dataarray]
c = [i[2] for i in dataarray]


x = np.array(a)
y = np.array(b)
z = np.array(c)'''



import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull 
import objectmaker 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
dataarray = objectmaker.run()


points= np.array(dataarray)

hull=ConvexHull(points)


x = [i[0] for i in points]
y = [i[1] for i in points]
z = [i[2] for i in points]
edges= [x,y,z]


for i in hull.simplices:
    plt.plot(points[i,0], points[i,1], points[i,2], 'r-')

ax.plot(edges[0],edges[1],edges[2],'bo') 

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')



plt.show()
print(edges)
