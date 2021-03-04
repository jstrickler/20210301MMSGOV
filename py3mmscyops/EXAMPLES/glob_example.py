#!/usr/bin/env python

from glob import glob

files = glob('../DATA/*.txt') # <1>
print(files, '\n')

no_files = glob('../DATA/*.possum')
print(no_files, '\n')

