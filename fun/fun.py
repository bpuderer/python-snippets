from collections import OrderedDict


# remove duplicates from iterable while preserving order
# https://stackoverflow.com/a/7961425    Raymond Hettinger
lst = [4, 1, 2, 1, 3, 3, 2, 4]
print("with duplicates removed, order maintained:", list(OrderedDict.fromkeys(lst)))


# remove duplicates from sorted list in place. easy, start from end
nums = [0, 0, 1, 2, 2, 2, 2, 2, 4, 4, 4]
for i in range(len(nums)-1, 0, -1):
    if nums[i] == nums[i-1]:
        del nums[i]
print(nums)
