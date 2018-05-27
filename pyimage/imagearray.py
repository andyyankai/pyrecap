# transform an image to 2d array
# currently convert all image to black and white for an easy start
# and do a reverse stuff
from PIL import Image
from numpy import*




def image2array(x):
    temp=asarray(Image.open(x))
    x=temp.shape[0]
    y=temp.shape[1]*temp.shape[2]


    return temp
    
def array2image(x):
    img = Image.new('1', (int(size(a[0])/3), int(size(a)/size(a[0]))))
    img = Image.fromarray(x, 'RGB')
    img.save('out.jpg')
    img.show()
		    
		    
a = image2array('bigtest.jpg')

print(a) 
array2image(a)

print(size(a)/size(a[0])) # this is the height of the image, for bigtest is 642.0
print(size(a[0])/3) # this is the width of the image, for bigtest is 4800

