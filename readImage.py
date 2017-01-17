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
