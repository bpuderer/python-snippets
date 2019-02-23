import json
from datetime import datetime

# dumps - serialization - object to string
# loads - deserialization - string to object

obj = {'_id': 0, 'things': [{'bool': True, 'float': 3.14, 'none': None}], 'tuple': (1, 2), 'str': 'str val', 'timestamp': datetime.now()}
# https://docs.python.org/3/library/json.html#json.dump
# default should be a function that gets called for objects that can't otherwise be serialized
obj_str = json.dumps(obj, default=str)

print("object:", obj)
print("\nserialized:", obj_str)
print("\ndeserialized (note tuple):", json.loads(obj_str))

# in py 3.4, if indent != None, separators=(',', ': ')
print("\nformatted:", json.dumps(obj, indent=2, sort_keys=True, default=str))


test_file = 'test.json'

with open(test_file, 'w') as f:
    print("serialized to", test_file)
    json.dump(obj, f, default=str)

with open(test_file) as f:
    print("deserialized from", test_file, json.load(f))
