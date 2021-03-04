import lxml.etree as et

doc = et.parse("DATA/solar.xml")  # Get ElementTree obj

for planet in doc.findall('.//planet'):
    print(planet.get("planetname"))
    for moon in planet.findall('.//moon'):
        print("\t{}".format(moon.text))
print("-" * 60)
for moon in doc.findall('.//moon'):
    print(moon.text)