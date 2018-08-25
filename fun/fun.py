from collections import OrderedDict


# remove duplicates from iterable while preserving order
# https://stackoverflow.com/a/7961425    Raymond Hettinger
lst = [4, 1, 2, 1, 3, 3, 2, 4]
print("with duplicates removed, order maintained:", list(OrderedDict.fromkeys(lst)))
