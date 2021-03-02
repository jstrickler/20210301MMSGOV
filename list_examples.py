list1 = list()  # new, empty, list
list2 = ['a', 'b', 'c']
list3 = []

cities = ['Philadelphia', 'New York', 'Boston']
print(cities)
print(cities[0], cities[2])
cities.append('Los Angeles')
cities.append('Detroit')
print(cities)
cities.insert(0, 'Portland')
cities.insert(3, 'Seattle')
print(cities)
more_cities = ['Topeka', 'Amarillo', 'Baton Rouge']
cities.extend(more_cities)
print(cities)

del cities[4]
print(cities)

city = cities.pop()
print(city)
print(cities)
city = cities.pop(4)
print(city)
print(cities)

cities.remove('Topeka')
print(cities)

print(cities[:3])
print(cities[2:10])

for city in cities:
    # city  = next_element_of cities
    print(city)
print()

actor = "Bob Newhart"

for ch in actor:
    print(ch, end=' ')
print()

for i in range(1, 11):
    print(i)

#  (for i = 1; i < 11; i++) {
#  }

for _ in range(5):
    print("whoohooo")

print(len(cities))
print(min(cities), max(cities))
print(sorted(cities))




