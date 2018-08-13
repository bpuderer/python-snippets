# https://docs.python.org/3/library/xml.etree.elementtree.html#xpath-support

import xml.etree.ElementTree as ET


ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}

tree = ET.parse('test.xml')
root = tree.getroot()

# root = ET.fromstring(test.xml_data_as_string)


# useful for seeing element namespaces of complicated docs
"""
print("Iterate entire tree:")
for e in root.iter():
    print(e.tag, e.attrib, e.text)
"""

for actor in root.iterfind('./real_person:actor', ns):
    print(actor.get('name'), "of", actor.findtext('./real_person:birthplace', namespaces=ns))
    for char in actor.iterfind('./role:character', ns):
        print(' |-->', char.text)


print("\nBirthplaces:")
# for birthplace in root.iterfind('./real_person:actor/real_person:birthplace', ns):
for birthplace in root.iterfind(".//real_person:birthplace", ns):
    print(birthplace.text)


# findall same as iterfind but returns list instead of iterable
print("\nWhich character(s) did Eric Idle play?")
for character in root.iterfind("./real_person:actor[@name='Eric Idle']/role:character", ns):
    print(character.text)


print("\nWhich actor(s) played King Arthur?")
for result in root.iterfind("./real_person:actor[role:character='King Arthur']", ns):
# *any* element which has character subelement set to King Arthur
#for result in root.iterfind(".//*[role:character='King Arthur']", ns):
    print(result.get('name'))


print("\nWhere are the actor(s) who played King Arthur from?")
for birthplace in root.findall("./real_person:actor[role:character='King Arthur']/real_person:birthplace", ns):
    print(birthplace.text)


# find returns a single element or None
print("\nFirst artist name:")
print(root.find(".//real_person:artist", ns).get('name'))


# modify
actor_cleese = root.find("./real_person:actor[@name='John Cleese']", ns)
actor_cleese.set('name', 'UPDATED name')
birthplace_cleese = actor_cleese.find("./real_person:birthplace", ns)
birthplace_cleese.text += ' UPDATED'

xml_str = ET.tostring(root, encoding='utf-8')
print(xml_str)

# tree.write('out.xml')
