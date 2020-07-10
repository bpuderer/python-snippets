import bisect
import random


# from https://docs.python.org/3.8/library/bisect.html
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    #raise ValueError
    return -1



lst = []
for _ in range(1, 13):
    num = random.randint(1, 10)
    # bisect, bisect_right are the same.  inserts are to the right
    # bisect_left also available
    position = bisect.bisect(lst, num)
    bisect.insort(lst, num)
    print(f'inserting {num} at {position}  updated list: {lst}')


lst = [-4, -1, 0, 2, 2, 28]
print(f'Location of 2 in {lst}: {index(lst, 2)}')
print(f'Location of 22 in {lst}: {index(lst, 22)}')
