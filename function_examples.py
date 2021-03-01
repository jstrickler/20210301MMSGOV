def spam():
    return 42

print(spam)
print(spam())
result = spam()

ham = spam
print(ham())

def triple(m):
    return m * 3

m1 = triple(5)
m2 = triple(8.99)
m3 = triple('threat')
m4 = triple(['a', 'b', 'c'])
print(m1, m2, m3, m4)

def addem(a, b):
    return a + b

def doit(a, *b):
    print("a:", a)
    print("b:", b)

doit(1)
doit(1, 2, 3, 4, 5, 6)

def hello(whom="world"):
    print("Hello,", whom)

hello('Mom')
hello()

def add_to_db(*, first_name, last_name):
    print(first_name, last_name)

add_to_db(first_name="Bob", last_name="Smith")
add_to_db(last_name="Addams", first_name="Gomez")

def config(**values):
    print(values)

config()
config(animal="wombat", filename="spam.txt", username="notappearinghere")

def wacky(p1, p2, *p3, p4, p5, **p6):
    pass











