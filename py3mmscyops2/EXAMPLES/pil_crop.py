#!/usr/bin/env python
from PIL import Image

box = (1200, 100, 2000, 400)  # <1>
im = Image.open('../DATA/felix_auto.jpeg')
region = im.crop(box)  # <2>
region = region.transpose(Image.FLIP_LEFT_RIGHT)  # <3>
im.paste(region,box)  # <4>
im.save('felix_auto_cropped.jpg')  # <5>
