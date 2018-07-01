# no switch/case
x = 3
if x < 0:
    print(x, "is negative")
elif x == 0:
    print(x, "is 0")
else:
    print(x, "is positive")


# conditional
print("trueval" if True else "falseval")
print("trueval" if False else "falseval")


# chained
if 1 < x < 5:
    print(x, "is between 1 and 5")
