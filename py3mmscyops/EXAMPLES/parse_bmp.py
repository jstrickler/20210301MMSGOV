#!/usr/bin/env python

from struct import Struct

# short int short short int (native, unsigned)
s = Struct('=2cI4xI')  # <1>

with open('../DATA/chimp.bmp', 'rb') as chimp_in:
    chimp_bmp = chimp_in.read(s.size)  # <2>

(signature1, signature2, size, offset) = s.unpack(chimp_bmp)  # <3>

print("signature:", signature1, signature2)  # <4>
print('size:', size)
print('offset:', offset)
print(list(chimp_bmp))
