import inspect

colors = ['red', 'blue', 'green']
print(type(colors))
print(help(colors))
print("-" * 60)

print(hasattr(colors, 'append'))
a = getattr(colors, 'append')
a('pink')
print(colors)

if hasattr(colors, 'tojson'):
    json = getattr(colors, 'tojson')()

b = "banana"
print(callable(a), callable(b))

mary = """
Mary had a little lamb;\t
Its fleece was white as snow.
And everywhere than Mary went
The lamb was sure to go
"""

print(mary, '\n')

print(repr(mary))

class Animal:
    pass

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

class Duck:
    pass

class Spam:
    pass

class Ham:
    pass

d = Dog()
c = Cat()
dk = Duck()

print(isinstance(d, (Dog, Spam, Ham)))
print(isinstance(d, Animal))
print(isinstance(dk, Animal))
print(issubclass(Dog, Animal))

class A:
    pass

class B(A):
    pass

print(issubclass(B, A))
print(isinstance(B, A))

def toast():
    pass

print(A.__name__)
print(toast.__name__)

def wacky(p1, p2="umbrella", *p3, p4, p5="artichoke", **p6):
    pass

spec = inspect.getfullargspec(wacky)

if len(spec.args) != 2:
    print("Function must have 2 positional parameters")
else:
    print("Carry on...")



#  dir()

print(dir(Dog))
print(dir(d))

print(dir(colors))





