d1 = dict()
d2 = {'a': 5, 'b': 10, 'm': 19}
d3 = {}
keys = ['NY', 'NC', 'NE']
values = ['Albany', 'Raleigh', 'Omaha']

print(list(zip(keys, values)))
sc = dict(zip(keys, values))
print(sc)

sc['CA'] = 'Sacramento'
sc['FL'] = "Tallahassee"

print(sc)
del sc['NE']
print(sc)

sc['NC'] = 'Durham'

print(sc)

print(sc['NC'])

for abbr in 'NC', 'NY', 'MS', 'TX':
    print(abbr, sc.get(abbr, 'NOT FOUND'))

print(len(sc))

print("AL" in sc)
print()

for state, capital in sc.items():
    print(state, capital)

print(sc.items())






