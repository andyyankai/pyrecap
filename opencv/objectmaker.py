import threeDpoint
import numpy as np
import math


'''
Rotation along X:
y' = y*cos(a) - z*sin(a)
z' = y*sin(a) + z*cos(a)
x' = x

Rotation along Y:
z' = z*cos(a) - x*sin(a)
x' = z*sin(a) + x*cos(a)
y' = y

Rotation along Z:
x' = x*cos(a) - y*sin(a)
y' = x*sin(a) + y*cos(a)
z' = z
'''       


mergedata = []



data = threeDpoint.get3d('./teddydata/01.png', './teddydata/02.png')
arrdata = np.asarray(list(data))
rotatedata = []
for i in arrdata:
	x = i[0]
	y = i[1]
	z = i[2]
	rotatedata.append([x, y, z])
mergedata += rotatedata

data = threeDpoint.get3d('./teddydata/18.png', './teddydata/19.png')
arrdata = np.asarray(list(data))
rotatedata = []
for i in arrdata:
	x = i[2]*math.sin(math.pi/2) + i[0]*math.cos(math.pi/2)+700
	y = i[1]
	z = i[2]*math.cos(math.pi/2) - i[0]*math.sin(math.pi/2)
	rotatedata.append([x, y, z])
mergedata += rotatedata
	


data = threeDpoint.get3d('./teddydata/36.png', './teddydata/37.png')
arrdata = np.asarray(list(data))
rotatedata = []
for i in arrdata:
	x = i[2]*math.sin(math.pi) + i[0]*math.cos(math.pi)+700
	y = i[1]
	z = i[2]*math.cos(math.pi) - i[0]*math.sin(math.pi)
	rotatedata.append([x, y, z])
mergedata += rotatedata
	



np.savetxt("out.obj", mergedata, delimiter=' ', newline='\nv ')

	
	
