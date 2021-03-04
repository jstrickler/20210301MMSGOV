#!/usr/bin/env python

from PIL import Image

size = 125, 125  # <1>
im = Image.open('../DATA/felix_auto.jpeg')
im.thumbnail(size)  # <2>
im.save('felix_auto_small.png')  # <3>
