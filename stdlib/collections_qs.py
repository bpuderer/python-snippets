from collections import defaultdict, OrderedDict, Counter, namedtuple, deque


# dict subclass with optional iterable or mapping on instantiation
# 0 returned instead of KeyError if missing
c = Counter("these are attack eyebrows")
print("3 most common", c.most_common(3))
print('"s" occurs', c['s'], 'times')

c = Counter()
c.update('b')
c.update({'b': 2})
print(c)

print('---')


# tuple subclass
# Raymond Hettinger, author of namedtuple
# https://www.youtube.com/watch?v=OSGv2VnC0go&t=32m19s
Name = namedtuple('Name', ['first', 'middle', 'last'])
def get_name():
    return Name('John', 'Marwood', 'Cleese')

name = get_name()
print(name.last, ', ', name.first, ' ', name.middle[0], sep='')
print(Name._make(['Michael', 'Edward', 'Palin'])) # new instance from iterable


print('---')


# dict subclass
# default_factory creates default value when key does not exist
# commonly used to append to lists in dictionaries

# grouping idiom
names = ['van Rossum', 'torvalds', 'stallman', 'thompson', 'ritchie', 'wall', 'gosling']

dd = defaultdict(list)
for name in names:
    dd[len(name)].append(name)
print(dd)


print('---')


# deque ("deck") - double ended queue
# use deque vs list when append/pop from ends
# O(1) vs O(n)

d = deque()            # can init with iterable and set maxlen
d.append('h')
d.appendleft('t')
d.extend('on*')
d.extendleft('yp-')    # notice order
print(d)
print('after removing', d.pop(), 'via pop():', d)
print('after removing', d.popleft(), 'via popleft():', d)


print('---')


# dict subclass, preserves order keys were added
# NOTE: dictionary order is now guaranteed to be insertion order
# https://docs.python.org/3/library/stdtypes.html#dict.values

od = OrderedDict()
od['a'] = 0
od['z'] = 1
od['b'] = 2
print(od)
