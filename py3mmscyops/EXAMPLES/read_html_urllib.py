#!/usr/bin/env python

import urllib.request

response = urllib.request.urlopen("https://www.python.org")

print(response.headers)  # <1>
print(response.headers.get('content-type'))
print()

print(response.read(500).decode())   # <2>

print(response.url)
print(response.status)
