import lxml.etree as et

doc = et.parse("DATA/solar.xml")  # Get ElementTree obj

root = doc.getroot()  # get top-level Element
print(root)
for child in root:
    if 'planets' in child.tag:
        for planet in child.findall('planet'):
            print(planet.get("planetname"))
            for moon in planet.findall('moon'):
                print("\t{}".format(moon.text))
