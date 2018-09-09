# no switch/case
x = 3
if x < 0:
    print(x, "is negative")
elif x == 0:
    print(x, "is 0")
else:
    print(x, "is positive")


# conditional expression
print("trueval" if True else "falseval")
print("trueval" if False else "falseval")

d = {'a': 1}
# d.get('b')*2  -> TypeError
print(d['a']*2 if 'a' in d else None)
print(d['b']*2 if 'b' in d else None)

# elif using conditional expression
# https://stackoverflow.com/a/9987533  Raymond Hettinger
# parentheses added for readability
l = [2, 1, 3, 1]
print(['one' if v==1 else ('two' if v==2 else 'not one or two') for v in l])


# chained
if 1 < x < 5:
    print(x, "is between 1 and 5")


# and, or are short-circuit operators
# or short-circuits after seeing a True value
# and short-circuits after seeing a False value
print(True or 5/0)
print(False and 5/0)
