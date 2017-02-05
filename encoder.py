# Copyright (c) 2016-present, Deckard, SoCrowd GmbH.
# All rights reserved.

# Read images

from PIL import Image

def readImage(filename):
    im = Image.open(filename)
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    return (pix,width,height)

def encodePrimax(filename):
    img = Image.new( 'RGB', (255,255), "black")
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i,j] = (i, j, 33)
    img.save(filename)
    img.show()

encodePrimax("dupa.bmp")
