fruits = ['apple', 'strawberry', 'banana', 'fig', 'kiwi', 'lemon',
          'pear', 'apricot', 'blueberry']

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]  # list comprehension
print("f1:", f1, '\n')

f2 = [f.upper() for f in fruits if f.startswith('b')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('b')]
print("f3:", f3, '\n')

attributes = [a for a in dir(fruits) if not a.startswith('__')]
print(attributes, '\n')

people = [
    ("Melinda", "Gates", "Gates Foundation", "1964-08-15"),
    ("Steve", "Jobs", "Apple", "1955-02-24"),
    ("Larry", "Wall", "Perl", "1954-09-27"),
    ("Paul", "Allen", "Microsoft", "1953-01-21"),
    ("Larry", "Ellison", "Oracle", "1944-08-17"),
    ("Bill", "Gates", "Microsoft", "1955-10-28"),
    ("Mark", "Zuckerberg", "Facebook", "1984-05-14"),
    ("Sergey", "Brin", "Google", "1973-08-21"),
    ("Larry", "Page", "Google", "1973-03-26"),
    ("Linus", "Torvalds", "Linux", 'Git', "1969-12-28"),
    ("John", "Smith", '1975-11-22'),
]

last_names = [p[1] for p in people]
print("last_names:", last_names, '\n')

fgen = (f.upper() for f in fruits)
print(fgen)

for fruit in fgen:
    print(fruit)

r = reversed(fruits)
print(r)

x = 123

def doit():
    print(x.upper())

def spam():
    doit()

def ham():
    spam()

ham()

for i, fruit in enumerate(fruits):
    print(i, fruit)

a = ['red', 'blue', 'green']
b = ['crab', 'moon', 'monster']
combo = zip(a, b)
print(combo)
for x, y in combo:
    print(x, y)





