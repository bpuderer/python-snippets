def has_unique_characters(data):
    return len(data) == len(set(data))

print(has_unique_characters("abcdebfg"))
print(has_unique_characters("abcdefg"))


s1 = set(['a', 'b', 'c'])
s1.add('a')
s1.add('d')
print(s1)

s2 = {1, 'a', 'kenny'}
print(s2)

print(f'union: {s1.union(s2)}')                    # also s1 | s2
print(f'intersection: {s1.intersection(s2)}')      # also s1 & s2
print(f'diff: {s1.difference(s2)}')                # also s1 - s2
# sym diff is their union minus the intersection
print(f'sym diff: {s1.symmetric_difference(s2)}')  # also s1 ^ s2


# remove throws KeyError if not in set, discard does not
s2.remove('kenny')
s2.discard('kenny')
print(s2)
