#!/usr/bin/env python
from PIL import Image # <1>

im = Image.open('../DATA/felix_auto.jpeg')  # <2>
print(im.format)  # <3>
print(im.size)  # <3>
print(im.mode)  # <3>

im.save('felix_auto.png')
