#important

import cv2
import numpy as np
from matplotlib import pyplot as plt


def fuse(dd):
	ret = []
	ret.append(dd[0])
	save = False
	for i in dd:
		save = True
		for j in ret:
			if abs(j[0]-i[0])<3 and abs(j[1]-i[1])<3:
				save = False
				break
		if save == True:
			ret.append(i)
		save = False
	return ret




filename = '01.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,1,0.04)

imgpoints = [] # 2d points in image plane.
print(img.shape)
 

#result is dilated for marking the corners, not important
#dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
img[dst<0.01*dst.max()]=[255,255,255]

height, width, depth = img.shape
for i in range(0, height):
    for j in range(0, int(width)):
    	if str(img[i,j]) != "[255 255 255]":
        	imgpoints.append([i,j,0])

a = fuse(imgpoints)
print(a)
dst = cv2.dilate(dst,None)
plt.imshow(img),plt.show()

