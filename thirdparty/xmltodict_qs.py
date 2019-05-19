import json

import xmltodict


simple_xml = """<?xml version="1.0" encoding="UTF-8"?>
<library name="Algiers Regional Library">
   <books>
      <book format="hardcover">
         <title>Wise Blood</title>
         <author format="First Name Last Name">Flannery O'Connor</author>
      </book>
      <book format="paperback">
         <title>The Moviegoer</title>
         <author format="First Name Last Name">Walker Percy</author>
      </book>
   </books>
</library>"""

library = xmltodict.parse(simple_xml)
print(json.dumps(library, indent=4))

print("Library name:", library['library']['@name'])
print(f"Titles: {[book['title'] for book in library['library']['books']['book']]}")


print('----')


xml_with_ns = """<?xml version="1.0" encoding="UTF-8"?>
<actors xmlns="http://people.example.com" xmlns:fictional="http://characters.example.com">
   <actor name="John Cleese">
      <birthplace>Weston-super-Mare, Somerset, England</birthplace>
      <fictional:character>Black Knight</fictional:character>
      <fictional:character>First Centurion</fictional:character>
      <fictional:character>Robin Hood</fictional:character>
      <fictional:character>Archie Leach</fictional:character>
   </actor>
   <actor name="Eric Idle">
      <birthplace>South Shields, County Durham, England</birthplace>
      <fictional:character>The Dead Collector</fictional:character>
      <fictional:character>Harry the Haggler</fictional:character>
      <fictional:character>Gunther</fictional:character>
      <fictional:character>Berthold</fictional:character>
   </actor>
   <actor name="Michael Palin">
      <birthplace>Broomhill, Sheffield, West Riding of Yorkshire, England</birthplace>
      <fictional:character>Sir Galahad</fictional:character>
      <fictional:character>Mr. Big Nose</fictional:character>
      <fictional:character>Jack Lint</fictional:character>
      <fictional:character>Ken Pile</fictional:character>
   </actor>
</actors>"""


# process_namespaces=False by default, ns defs are just attribs
# optional namespaces arg allows shorthand defs and None is treated as the default ns
# NOTE: namespace dict reverses keys and values as seen in ElementTree Element.findall()
ns = {'http://people.example.com': None, 'http://characters.example.com': 'role'}
actors_ns = xmltodict.parse(xml_with_ns, process_namespaces=True, namespaces=ns)
print(json.dumps(actors_ns, indent=4))

for actor in actors_ns['actors']['actor']:
    print(f"{actor['@name']}: {[role for role in actor['role:character']]}")


print("\n***dict to xml***\n")


# reverse, dict to xml
# can also pass collections.OrderedDict
simple_dict = {
    "library": {
        "@name": "Algiers Regional Library",
        "books": {
            "book": [{
                "@format": "hardcover",
                "title": "Wise Blood",
                "author": {
                    "@format": "First Name Last Name",
                    "#text": "Flannery O'Connor"
                }
            }, {
                "@format": "paperback",
                "title": "The Moviegoer",
                "author": {
                    "@format": "First Name Last Name",
                    "#text": "Walker Percy"
                }
            }]
        }
    }
}
print(xmltodict.unparse(simple_dict, pretty=True))


print('----')


ns_dict = {
    "actors": {
        "@xmlns": "http://people.example.com",
        "@xmlns:fictional": "http://characters.example.com",
        "actor": [
            {
                "@name": "John Cleese",
                "birthplace": "Weston-super-Mare, Somerset, England",
                "fictional:character": [
                    "Black Knight",
                    "First Centurion",
                    "Robin Hood",
                    "Archie Leach"
                ]
            },
            {
                "@name": "Eric Idle",
                "birthplace": "South Shields, County Durham, England",
                "fictional:character": [
                    "The Dead Collector",
                    "Harry the Haggler",
                    "Gunther",
                    "Berthold"
                ]
            },
            {
                "@name": "Michael Palin",
                "birthplace": "Broomhill, Sheffield, West Riding of Yorkshire, England",
                "fictional:character": [
                    "Sir Galahad",
                    "Mr. Big Nose",
                    "Jack Lint",
                    "Ken Pile"
                ]
            }
        ]
    }
}
print(xmltodict.unparse(ns_dict, pretty=True))
