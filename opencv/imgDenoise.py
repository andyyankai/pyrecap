import numpy as np
import cv2
from matplotlib import pyplot as plt
import glob



images = glob.glob('*.jpg')

i=1

for fname in images:
	img = cv2.imread(fname)
	i=i+1
	dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

	cv2.imwrite(str(i)+'.jpg',img)
