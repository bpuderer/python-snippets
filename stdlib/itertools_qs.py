import itertools

# https://docs.python.org/3/library/itertools.html#itertools-recipes


# vs zip() which stops when shortest exhausted
print('zip_longest:', list(itertools.zip_longest('abc', '12')))

# chain can be used to flatten
print('chain:', list(itertools.chain('abc', ['x'], 'yz')))

print('combinations:', list(itertools.combinations('abc', 2)))
print('permutations:', list(itertools.permutations('abc', 2)))
print('Cartesian product:', list(itertools.product('abc', 'xy')))

# count, cycle, repeat are infinite iterators
# https://stackoverflow.com/a/2970789    Alex Martelli
i = itertools.cycle('abc')
for _ in itertools.repeat(None, 5):
    print(next(i))
