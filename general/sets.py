# unordered collection of unique, immutable objects

# set() for empty set, not {} which is empty dict
s1 = {'purple', 'green', 'gold'}
s2 = {'black', 'gold'}
t = ('maroon', 'white')

print('s1:', s1, 's2:', s2, 't:', t)
print('green in s1:', 'green' in s1)


# operator versions require args to be sets
# issubset, issuperset, union, intersection, difference, symmetric_difference
print('s1, s2 union:', s1 | s2)
print('s1, s2 intersection:', s1 & s2)
print('s1, s2 difference:', s1 - s2)
print('s1, s2 symmetric difference:', s1 ^ s2)


# disjointed if intersection is empty set
print('are s1, t disjoint?', s1.isdisjoint(t))


# |=, &=, -=, ^=
# update, intersection_update, difference_update, symmetric_difference_update
s1.update(s2, t)
print('s1 updated with s2 and t:', s1)


s1.remove('maroon') # KeyError if not in set
s1.discard('white')
print('s1 with maroon, white removed:', s1)


s3 = s1.copy() # shallow
s3.add('navy blue')
print('s3 is copy of s1 with navy blue added:', s3)


# also >=, issuperset
print('s3 a subset of s1?', s3 <= s1)
print('s1 a subset of s3?', s1.issubset(s3))


# clear to remove all elements from set
s1.clear()
print('s1 cleared:', s1)
