x = 5   # int x = 5;

print(x)

result = x * 10

print(result)
print(x, type(x), id(x))

y = x

print(y, type(y), id(y))

x = 10
print(x, y)
print(id(x), id(y))

y = 10

print(id(x), id(y))

x = "wombat"  # bind 'x' to str obj
w = x  # bind 'w' to str obj

print(x, type(x))
x = 123.456
print(x, type(x))

x, y, z = 5, 10, 15
m = n = r = 12








