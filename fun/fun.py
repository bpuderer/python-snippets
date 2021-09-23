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


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f'5! = {factorial(5)}')


def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n - 1) + fib(n - 2))

for n in range(10):
    print(fib(n))


def is_balanced(test_str):
    matching_start = {'}': '{', ']': '[', ')': '('}
    stack = []
    for char in test_str:
        if char in ['{', '(', '[']:
            stack.append(char)
        elif char in ['}', ')', ']']:
            if stack and stack[-1] == matching_start[char]:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True

tests = ('()', '{{}}', '{(})')
for test in tests:
    print(f'{test}: {is_balanced(test)}')
