import sys

# NOP
pass

a, b = 1, 2
print(a, b, "swapped ", end='')
a, b = b, a
print(a, b)


n = None
print("use 'is' and 'is not' to check for None, not equality:",
      n is not None)


# iterable unpacking PEP 3132
s = "python"
first, *middle, last = s
print("iterable unpacking:", first, middle, last)


# PEP 238 /=division //=floor
print("5/3:", 5/3, "5//3:", 5//3)


# remove from namespace
del s


print('module search paths:', sys.path)


# raises AssertionError if false
assert 1 in [1, 2], "some message"
