x = 3
if x < 0:
    print(x, "is negative")
elif x == 0:
    print(x, "is 0")
else:
    print(x, "is positive")


# PEP 634 Structural Pattern Matching
# comparing against literals
match x:
    case 1 | 2:
        print("x is 1 or 2")
    case 3:
        print("x is 3")
    case _:
        print("x is not 1, 2 or 3")

# directly from PEP 636. bind variables
point = (0, 5)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")



# conditional expression PEP 308.  ternary
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
