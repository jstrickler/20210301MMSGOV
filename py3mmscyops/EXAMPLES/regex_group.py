#!/usr/bin/env python

import re

s = """lorem ipsum M-302 dolor sit amet, consectetur r-99 adipiscing elit, sed do
 eiusmod tempor incididunt H-476 ut labore et dolore magna Q-51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z-883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A-110 cupidatat non proident, sunt in H-332 culpa qui 
officia deserunt Y-45 mollit anim id est laborum"""

#        2           xxxxxx
#        1   xxxxx
#        0  xxxxxxxxxxxxxxxxx
pattern = r'([A-Z])-(\d{2,3})'  # <1>

for m in re.finditer(pattern, s):
    print(m.group(0), m.group(1), m.group(2))  # <2>
    print(m.start(1), m.end(1), m.span())
print()

matches = re.findall(pattern, s)  # <3>
print("matches:", matches)

#  ssn = r'\d{3}-\d{2}-(\d{4})'

#  ssn = r'(\d{3})(?P<sep>[^\d\s])(\d{2})(?P=sep)(\d{4})']]

#  r'\d{10}(?=[:;])'
#  r'\d{10}(?![a-z])'




