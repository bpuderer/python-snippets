import sys

# NOP
pass

a, b = 1, 2
print(a, b, "swapped ", end='')
a, b = b, a
print(a, b)


# PEP 572 assignment expression, walrus operator
# TODO


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


print('PEP 515 underscores in numeric literals:', 1_000_000)


# anonymous function
# https://www.artima.com/weblogs/viewpost.jsp?thread=98196
print(list(map(lambda x: x + 2, [7, 11])))

# sort by last name
players = ['Drew Brees', 'Archie Manning', 'Bobby Hebert', 'Aaron Brooks']
print(sorted(players, key=lambda n: n.split()[-1]))

# no arg lambda that returns True - lambda: True


# __init__.py files are required to make py treat dirs containing file(s) as packages
# can be empty or contain init code for the pkg

# if __name__ == "__main__":
# execute when run as script, not imported

# mro - method resolution order
