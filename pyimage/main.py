# transform an image to 2d array
# currently convert all image to black and white for an easy start
from PIL import Image
from numpy import*


def image2array(x):
    temp=asarray(Image.open(x))
    print(temp)
    x=temp.shape[0]
    y=temp.shape[1]*temp.shape[2]

    temp.resize((x,y)) # a 2D array

    return temp
    
def array2image(x):
    img = Image.new('1', (64, 64))
    #img.putdata(x)
    img.save('out.jpg')
    img.show()
		    
		    
a = image2array('bigtest.jpg')
array2image(a)
print(size(a)/size(a[5])) # this is the height of the image, for bigtest is 642.0
print(size(a[5])) # this is the width of the image, for bigtest is 4800
print(size(a[1]))
