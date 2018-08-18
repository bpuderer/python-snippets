import xml.etree.ElementTree as ET
import xml.dom.minidom


actors_to_add = [{'name': 'John Cleese', 'birthplace': 'Weston-super-Mare, Somerset, England',
                  'characters': ['The Black Knight', 'First Centurion', 'Robin Hood', 'Archie Leach']}]

ET.register_namespace('', 'http://people.example.com')
ET.register_namespace('fictional', 'http://characters.example.com')

actors = ET.Element('{http://people.example.com}actors')

for actor_to_add in actors_to_add:
    actor = ET.SubElement(actors, 'actor', attrib={'name': actor_to_add['name']})
    # actor = ET.SubElement(actors, 'actor')
    # actor.set('name', actor_to_add['name'])
    birthplace = ET.SubElement(actor, 'birthplace')
    birthplace.text = actor_to_add['birthplace']
    for character_to_add in actor_to_add['characters']:
        character = ET.SubElement(actor, '{http://characters.example.com}character')
        character.text = character_to_add


xml_str = ET.tostring(actors, encoding='utf-8')
formatted_xml = xml.dom.minidom.parseString(xml_str).toprettyxml(indent='   ')
print(formatted_xml)
