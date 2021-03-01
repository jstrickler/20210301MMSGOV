
x = None
print(x, type(x), id(x))

y = None


if x is None:
    print("Wahoooo")

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a), id(b))
print(a == b, a is b)

def spam():
    name = 'Nellie'

x = spam()
print(x, type(x))




