from collections import namedtuple
import math
import string


# PEP 3101 Advanced strings formatting
print("and {} for {} completely {}".format("now", "something", "different"))
# simple field names: names or numbers
print("and {when} for {1} completely {0}".format("different", "something", when="now"))

# compount field name, . or []
Point = namedtuple('Point', ['x', 'y'])
p = Point(-1.0, y=-2.0)
print("x={0.x} y={0.y}".format(p))

movie = {'title': 'Life of Brian', 'director': 'Terry Jones', 'year': 1979}
print("{0[title]} directed by {0[director]} was released in {0[year]}".format(movie))

# https://docs.python.org/3/library/string.html#formatstrings
print("{:0>+8.3f}".format(math.pi))


# PEP 498 Literal String Interpolation
# Formatted string literals, aka f-strings
# f or F. {expression}
print(f'Pi: {math.pi:.5f}')



# concat strings in iterable using separator
print('-'.join('abcd'))

# https://stackoverflow.com/a/9061024
# list comprehension faster and more memory efficient than
# generator expression for str.join
print(''.join([str(i) for i in range(10)]))


print('str literals next to each other' ' are combined')

print('42 padded to 5:', '42'.zfill(5))


# use in operator to check if substring
# find returns -1 if not found, index raises ValueError
s = '867-5309'
print('53 is at location:', s.find('53'), 'in', s)


# startswith, endswith
s = '/dev/null'
t = ('\\', '/')
print(s, 'startswith', t, ':', s.startswith(t))
print(s, 'endswith', 'z:', s.endswith('z'))


# split, lsplit, rsplit, splitlines. can specify max # splits
s = 'and now for something completely different'
print(s, 'split:', s.split())
print(s, 'split on something:', s.split('something'))


# replace all occurrences. can specify # replacements
s = 'hello world'
print(s, 'with world replaced with Guido:', s.replace('world', 'Guido'))


# several is* methods, plus many string constants
s = '00157'
print(s, 'is digit:', s.isdigit())
s = 'ABC123'
print(s, 'contains all hex chars:', all(c in string.hexdigits for c in s))


# lower, upper
s = 'You\'re using coconuts!'
print(s, 'uppercased:', s.upper(), 'lowercased:', s.lower())


# strips. remove whitespace though string can be provided. lstrip, rstrip
s = '\n\t\t Norwegian Blue  '
print('Before:', s, 'After strip:', s.strip())


# raw string. useful for regex
print(r'\n\t\n\t')
