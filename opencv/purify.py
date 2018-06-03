from PIL import Image
import numpy as np
import glob


def purify(filename):
	col = Image.open(str(filename))
	gray = col.convert('L')

	# Let numpy do the heavy lifting for converting pixels to pure black or white
	bw = np.asarray(gray).copy()

	# Pixel range is 0...255, 256/2 = 128
	bw[bw < 128] = 0    # Black
	bw[bw >= 128] = 255 # White

	# Now we put it back in Pillow/PIL land
	imfile = Image.fromarray(bw)
	imfile.save(str(filename)+"purify.jpg")
	

images = glob.glob('*.jpg')

for fname in images:
	purify(fname)
