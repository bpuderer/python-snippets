# add/pop at end of list is fast, slow from beginning of list
# see collections.deque

lst = []
lst.append(0)
lst.extend((2, 3, 4)) # appends items in iterable
lst.insert(1, "one")
print("lst:", lst)

# can also use optional range specified using slice notation
print("\"one\" is located at index:", lst.index("one"))

lst.remove("one") # ValueError if not in list, removes first occurrence
lst.pop(0) # remove and return val at optional index or last if not specified
del lst[0]
print("lst:", lst)

lst_copy = lst.copy() # shallow copy
lst.clear() # del lst[:]
print("lst:", lst, "lst_copy", lst_copy)

# reverse, sort for in place reversing, sorting

lst1 = [1, 2]
lst2 = [3, 4]
print("lst1:", lst1, "lst2:", lst2, "combined:", lst1+lst2)

# PEP 448
lst1 = [1, 2]
lst2 = [3, 4]
tup1 = (5, 6)
set1 = {7, 8}
print("lst1:", lst1, "lst2:", lst2, "tup1:", tup1, "set1:", set1,
      "combined:", [*lst1, *lst2, *tup1, *set1])
