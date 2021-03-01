import sys
import time
import re

print(sys.prefix)
print(sys.executable, '\n')

print(sys.platform, '\n')  # linux darwin win32

for path in sys.path:
    print(path)
print()

print(sys.modules['time'])
print(sys.modules['re'])

