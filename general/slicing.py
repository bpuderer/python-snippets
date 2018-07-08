# [start:stop:step]

s = "Monty Python's Flying Circus"

print("entire sequence:", s[:])
print("last element:", s[-1])
print("reversed:", s[::-1])

print("third to end:", s[2:])
print("last three:", s[-3:])
print("first three:", s[:3])
print("beginning until last three:", s[:-3])
print("ever other element:", s[::2])

print("third through fifth:", s[2:5])
# start and stop relative to direction
print("third through fifth reversed:", s[4:1:-1])

# naming slices
last_three_reversed = slice(None, -4, -1)
print("last three reversed:", s[last_three_reversed])


# slice assignment to insert
lst = ['and', 'completely', 'different']
lst[1:1] = ['now', 'for', 'something']
print(lst)


# remove adjacent items from list
lst = ['and', 'now', 'for', 'something',
       'this', 'is', 'an', 'ex-parrot',
       'completely', 'different']
del lst[4:8]
print(lst)


# replace adjacent items in list
lst = ['and', 'now', 'for', 'everything', 'somewhat', 'different']
lst[3:5] = ['something', 'completely']
print(lst)


# why end is excluded
print('Python'[:2], 'Python'[2:], sep='')
