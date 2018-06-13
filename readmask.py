from PIL import Image

def getdict():

    im = Image.open('mask.jpg', 'r')

    pix_data = list(im.getdata())

    width, height = im.size

    data = {}

    w = 0
    h = 0

    for pix in pix_data:
        if w == 649:
            h += 1
            w = 0
        else:
            w += 1
        data[(w,h)] = pix

    return data

