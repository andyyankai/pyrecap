from PIL import Image
import cv2
import glob


images = glob.glob('./teddydata/*.png')

count = 0
for fname in images:
	img = Image.open(fname)
	area = (950, 350, 1600, 1300)
	cropped_img = img.crop(area)
	cropped_img.save('./out/'+fname)
	count += 1
