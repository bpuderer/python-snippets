import json
from json import JSONEncoder
from datetime import datetime


# dumps - serialization - object to string
# loads - deserialization - string to object

obj = {'_id': 0, 'things': [{'bool': True, 'float': 3.14, 'none': None}], 'tuple': (1, 2), 'str': 'str val', 'timestamp': datetime.now()}
# https://docs.python.org/3/library/json.html#json.dump
# default should be a function that gets called for objects that can't otherwise be serialized
# obj_str = json.dumps(obj)    # TypeError: Object of type datetime is not JSON serializable
obj_str = json.dumps(obj, default=str)

print(f'object: {obj}')
print(f'\nserialized (dumps): {obj_str}')
print(f'\ndeserialized (loads) NOTE: tuple is now a list!!: {json.loads(obj_str)}')

# in py 3.4, if indent != None, separators=(',', ': ')
print(f'\nformatted serialization: {json.dumps(obj, indent=2, sort_keys=True, default=str)}')



test_file = 'test.json'
with open(test_file, 'w') as f:
    print(f'\n\nserialized (dump) to {test_file}')
    json.dump(obj, f, default=str)

with open(test_file) as f:
    print(f'deserialized (load) from {test_file} {json.load(f)}')



class MyClass:
    def __init__(self, name):
        self.name = name

class MyClassEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == MyClass:
            return o.name
        return super().default(o)

my_dict = {'g': MyClass('Guido')}
# obj_str = json.dumps(my_dict)  # TypeError: Object of type MyClass is not JSON serializable
# obj_str = json.dumps(my_dict, default=str)  # prints {"g": "<__main__.MyClass object at 0x7f4461d1ea10>"}
obj_str = json.dumps(my_dict, cls=MyClassEncoder)
print(f'\n\nobject: {my_dict}')
print(f'serialized: {obj_str}')
