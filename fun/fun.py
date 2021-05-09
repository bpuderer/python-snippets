from collections import OrderedDict


# remove duplicates from iterable while preserving order
# https://stackoverflow.com/a/7961425    Raymond Hettinger
lst = [4, 1, 2, 1, 3, 3, 2, 4]
print("with duplicates removed, order maintained:", list(OrderedDict.fromkeys(lst)))


# remove duplicates from sorted list in place. easy, start from end.  bad idea in general
nums = [0, 0, 1, 2, 2, 2, 2, 2, 4, 4, 4]
for i in range(len(nums)-1, 0, -1):
    if nums[i] == nums[i-1]:
        del nums[i]
print(nums)



def allow_one_duplicate_in_sorted_nums_list(nums):
    seen_it = False
    for i in range(len(nums)-1, 0, -1):
        if nums[i] != nums[i-1]:
            seen_it = False
        elif nums[i] == nums[i-1] and not seen_it:
            seen_it = True
        elif nums[i] == nums[i-1] and seen_it:
            del nums[i]
    return len(nums)


tests = (([], []),
        ([1], [1]),
        ([1, 1], [1, 1]),
        ([1, 1, 1], [1, 1]),
        ([0, 0, 0, 1, 2, 2, 2, 2, 2, 4], [0, 0, 1, 2, 2, 4]),
        ([0, 0, 1, 2, 2, 2, 2, 2, 3, 4, 4], [0, 0, 1, 2, 2, 3, 4, 4]),
        ([0, 1, 2, 2, 2, 2, 2, 4, 4, 4], [0, 1, 2, 2, 4, 4]))
for test in tests:
    allow_one_duplicate_in_sorted_nums_list(test[0])
    assert test[0] == test[1], f'Expected: {test[1]} Actual: {test[0]}'
