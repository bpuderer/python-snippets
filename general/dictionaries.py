# keys are unique, immutable
# if key is tuple, cannot contain mutable type

d = {'a': 0}
d = dict(a=0)
d = dict(zip('ab', range(2)))
print("d:", d)

print("is there a key named z:", 'z' in d)

print("value of a:", d['a']) # KeyError if not in map
print("value of z:", d.get('z')) # default optional

d['c'] = 2

# iterate over keys
for k in d:
    print(k, end=' ')
print()

# iterate over keys, vals
# dict.items, dict.keys, dict.values return view objects
# https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
for k, v in d.items():
    print(k, ":", v)

print("keys:", d.keys())
print("vals:", d.values())


del d['c'] # KeyError if not in map

# remove key and return val, KeyError if not in map
# and default val not specified
print("value of z:", d.pop('z', "default"))


# shallow copy, see copy.deepcopy
# d_copy = dict(d)
d_copy = d.copy()

d.clear()

print("d:", d, "d_copy:", d_copy)


# if key in dict, return val
# if not insert with opt defaut and return default
# can be used to init mutable dict vals
d.setdefault('list key', []).append('val')
d.setdefault('key')
print("d:", d)


d = dict(a=0, b=1)
d.update(b=11, c=2) # update, overwriting
d.update({'a': -1})
d.update([('a', -2), ['b', 111]])
print("d:", d)


# merge dicts using PEP 448
d1 = {'a': 0, 'b': 1}
d2 = {'a': -1, 'c': 2}
print("d1:", d1, "d2:", d2, "merged:", {**d1, **d2})


# flip/invert keys, values of a dict
print(f'{d} with keys/values flipped: { {v: k for k, v in d.items()} }')
