# Copyright (c) 2016-present, Deckard, SoCrowd GmbH.
# All rights reserved.

# Read images

from PIL import Image
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def readImage(filename):
    im = Image.open(filename)
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    return (pix,width,height)

def primeLexEncode(prime,lex):
    return ( (prime*lex^2) % 255, (prime*lex^2) % 255, (prime*lex^2) % 255)

def encodePrimax(arr,filename,mode):
    img = Image.new( 'RGB', (255,255), "black")
    pixels = img.load()

    if mode == "dist":
        for i in range(img.size[0]):
            if (i in arr.keys()):
                for j in range(img.size[1]):
                    pixels[i,j] = primeLexEncode(i,arr[i])
            else:
                for j in range(img.size[1]):
                    pixels[i,j] = (0,0,0)
        img.save(filename)
        #img.show()
    elif mode == "bright":
        for i in range(img.size[0]):
            if (i in arr.keys()):
                for j in range(img.size[1]):
                    pixels[i,j] = ( 0,0,0 )
            else:
                for j in range(img.size[1]):
                    pixels[i,j] = (i,j,(i+j) % 255)
        img.save(filename)
        #img.show()
    elif mode == "bright2":
        for i in range(img.size[0]):
            if (i in arr.keys()):
                for j in range(img.size[1]):
                    pixels[i,j] = ( i,j,i*j % 255)
            else:
                for j in range(img.size[1]):
                    pixels[i,j] = (i,j,(j) % 255)
        img.save(filename)
        #img.show()
