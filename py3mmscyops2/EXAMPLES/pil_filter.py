#!/usr/bin/env python
from PIL import Image, ImageFilter, ImageEnhance  # <1>

SMALLSIZE = 240,160  # <2>
im = Image.open('../DATA/felix_auto.jpeg')
im_small = im.resize(SMALLSIZE)  # <3>

im_emboss = im_small.filter(ImageFilter.EMBOSS)  # <4>
im_emboss.save('felix_auto_emboss.jpg')  # <5>

im_blur = im_small.filter(ImageFilter.BLUR)  # <6>
im_blur.save('felix_auto_blur.jpg')

enh_bright = ImageEnhance.Brightness(im_small)
im_bright = enh_bright.enhance(2.5)
im_bright.save('felix_auto_bright.jpg')

enh_lowcontrast = ImageEnhance.Contrast(im_small)
im_lowcontrast = enh_bright.enhance(.5)
im_lowcontrast.save('felix_auto_lowcontrast.jpg')
