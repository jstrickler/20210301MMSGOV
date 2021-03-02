import sys

print(sys.argv)
print(sys.argv[0])

for arg in sys.argv[1:]:  # loop over args
    print("arg:", arg)
