from PIL import Image
import cv2



img = Image.open("02.jpg")
area = (950, 350, 1600, 1300)
cropped_img = img.crop(area)
cropped_img.save("02out.jpg")
