import lxml.etree as et

root = et.Element('knights')

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        name, title, color, quest, comment = raw_line.rstrip().split(':')
        k = et.SubElement(root, 'knight', title=title)
        c = et.SubElement(k, 'color')
        c.text = color
        et.SubElement(k, 'quest').text = quest
        et.SubElement(k, 'comment').text = comment

print(et.tostring(root, pretty_print=True, xml_declaration=True).decode())

doc = et.ElementTree(root)
doc.write('knights.xml', xml_declaration=True, pretty_print=True)