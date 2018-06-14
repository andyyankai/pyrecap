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
def run():

	mergedata = []



	print("Loading data...", end="", flush=True)
	for j in range(1,71):
		print("%", end="", flush=True)
		data = threeDpoint.get3d('./teddydata/'+str(j)+'.png', './teddydata/'+str(j+1)+'.png')
		arrdata = np.asarray(list(data))
		rotatedata = []
		for i in arrdata:
			x = i[2]*math.sin(j/36*math.pi) + i[0]*math.cos(j/36*math.pi)+350*math.cos(j/36*math.pi+9*math.pi)+350
			y = i[1]
			z = i[2]*math.cos(j/36*math.pi) - i[0]*math.sin(j/36*math.pi)+350*math.sin(j/36*math.pi)
			rotatedata.append([x, y, z])
		mergedata += rotatedata

	print("Done! Check the out.obj for the points!")


	'''data = threeDpoint.get3d('./teddydata/1.png', './teddydata/2.png')
	arrdata = np.asarray(list(data))
	rotatedata = []
	for i in arrdata:
		x = i[2]*math.sin(0/36*math.pi) + i[0]*math.cos(0/36*math.pi)+350*math.cos(1/36*math.pi+9*math.pi)+350
		y = i[1]
		z = i[2]*math.cos(0/36*math.pi) - i[0]*math.sin(0/36*math.pi)+350*math.sin(1/36*math.pi)
		rotatedata.append([x, y, z])
	mergedata += rotatedata

	data = threeDpoint.get3d('./teddydata/18.png', './teddydata/19.png')
	arrdata = np.asarray(list(data))
	rotatedata = []
	for i in arrdata:
		x = i[2]*math.sin(18/36*math.pi) + i[0]*math.cos(18/36*math.pi)+350*math.cos(18/36*math.pi+9*math.pi)+350
		y = i[1]
		z = i[2]*math.cos(18/36*math.pi) - i[0]*math.sin(18/36*math.pi)+350*math.sin(18/36*math.pi)
		rotatedata.append([x, y, z])
	mergedata += rotatedata



	data = threeDpoint.get3d('./teddydata/36.png', './teddydata/37.png')
	arrdata = np.asarray(list(data))
	rotatedata = []
	for i in arrdata:
		x = i[2]*math.sin(36/36*math.pi) + i[0]*math.cos(36/36*math.pi)+350*math.cos(36/36*math.pi+9*math.pi)+350
		y = i[1]
		z = i[2]*math.cos(36/36*math.pi) - i[0]*math.sin(36/36*math.pi)+350*math.sin(36/36*math.pi)
		rotatedata.append([x, y, z])
	mergedata += rotatedata

	data = threeDpoint.get3d('./teddydata/54.png', './teddydata/55.png')
	arrdata = np.asarray(list(data))
	rotatedata = []
	for i in arrdata:
		x = i[2]*math.sin(54/36*math.pi) + i[0]*math.cos(54/36*math.pi)+350*math.cos(54/36*math.pi+9*math.pi)+350
		y = i[1]
		z = i[2]*math.cos(54/36*math.pi) - i[0]*math.sin(54/36*math.pi)+350*math.sin(54/36*math.pi)
		rotatedata.append([x, y, z])
	mergedata += rotatedata'''
		



	np.savetxt("out.obj", mergedata, delimiter=' ', newline='\nv ', header = 'nnnnnnnn')
	#return mergedata

	
	
