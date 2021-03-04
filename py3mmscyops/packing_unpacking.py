
values = [5, 10, 15, 20, 25, 30]
a, b, *c = values
print(a, b, c)
a, *b, c = values
print(a, b, c)
*a, b, c = values
print(a, b, c)
print()

data = [('a', 1), ('b', 2), ('c', 3)]

for letter, number in data:
    # letter, number = <next-element>
    print(letter * number)
print()

for i, value in enumerate(values):
    print(i, value)
print()
airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

for code, name in airports.items():
    print(code, name)
print()



people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for first_name, last_name, *_ in people:
    print(first_name, last_name)
print()

def combine(a, b, c):
    return a + b + c

print(combine(1, 5, 19))
print(combine('a', 'n', 'p'))

junk = [5, 10, 15]

print(combine(*junk), '\n')

data = [
    (1, 2, 3),
    (8, 10, 12),
    (37, 41, 15),
    (0, 99, 5.23),
]
for d in data:
    print(combine(*d))
print()














