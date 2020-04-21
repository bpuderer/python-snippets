# From PSF docs: A list comprehension consists of brackets containing
# an expression followed by a for clause, then zero or more for or if clauses.
print("List comprehension:")
print("squares of numbers divisible by 3 in [0..10]:", [i**2 for i in range(11) if i % 3 == 0])

lst = [[0, 1], [2], [], [3, 4, 5]]
print(lst, "flattened:", [item for sublist in lst for item in sublist])

# later for clause nested in earlier for clause
print("nested:", [(x, y) for x in range(3) for y in range(2)])

words = ['foo', 'bar', 'baz']
print("conditional:", [word.upper() if word.startswith('b') else word for word in words])


print("----\nDictionary comprehension:")
d = {'key1': 'val1', 'key2': 'val2'}
print(d, "keys and vals flipped:", {v: k for k, v in d.items()})


print("----\nSet comprehension:")
words = ['the', 'The', 'THE', 'then', 'Then', 'THEN']
print("set of", words, "lowercased:", {word.lower() for word in words})
