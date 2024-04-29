# linear
def linear_search(data, val):
    for i, item in enumerate(data):
        if item == val:
            return i
    return -1


# binary search.  divide/decrease and conquer O(log n)
# decrease and conquer - decreases by a constant value or by a constant factor or by a variable amount
def binary_search(data, target):
    low_ptr = 0
    high_ptr = len(data) - 1

    while low_ptr <= high_ptr:
        mid_ptr = (low_ptr + high_ptr) // 2
        if data[mid_ptr] == target:
            return mid_ptr
        elif data[mid_ptr] < target:
            low_ptr = mid_ptr + 1
        else:
            high_ptr = mid_ptr - 1
    return -1

lst = [1, 5, 20, 30, 30, 31, 40, 41, 60, 79]
assert binary_search(lst, 41) == 7
assert binary_search(lst, 30) == 3 or binary_search(lst, 30) == 4
assert binary_search(lst, 33) == -1
