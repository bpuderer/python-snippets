from collections import Counter


def my_counter(iterable):
    d = {}
    for item in iterable:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d


# remove duplicates from sequence while preserving order
# https://stackoverflow.com/a/7961425    Raymond Hettinger
lst = [4, 1, 2, 1, 3, 3, 2, 4]
#print("with duplicates removed, order maintained:", list(OrderedDict.fromkeys(lst)))
# Python 3.7 insertion order preserved with dicts - June 27 2018
print("with duplicates removed, order maintained:", list(dict.fromkeys(lst)))



# remove duplicates from sorted list in place. non-decreasing order.  easy, start from end.
def remove_duplicates_in_place(nums):
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i]

nums = [0, 0, 1, 2, 2, 2, 2, 2, 4, 4, 4]
remove_duplicates_in_place(nums)
print(nums)


def remove_duplicates_in_place_unsorted(nums):
    seen = set()
    for i in range(len(nums)-1, -1, -1):
        if nums[i] in seen:
            del nums[i]
        else:
            seen.add(nums[i])


def remove_duplicates_in_place_unsorted_better(nums):
    seen = set()
    write_index = 0

    for num in nums:
        if num not in seen:
            seen.add(num)
            nums[write_index] = num
            write_index += 1

    del nums[write_index:]

nums = [0, 5, 4, 5, 1, 2, 1, 2, 5, 7, 0]
remove_duplicates_in_place_unsorted(nums)
print(nums)
nums = [0, 5, 4, 5, 1, 2, 1, 2, 5, 7, 0]
remove_duplicates_in_place_unsorted_better(nums)
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



def is_balanced(test_str):
    matching_start = {'}': '{', ']': '[', ')': '('}
    stack = []
    for char in test_str:
        if char in '{([':
            stack.append(char)
        elif char in '})]':
            if stack and stack[-1] == matching_start[char]:
                stack.pop()
            else:
                return False
    return not stack

tests = ('()', '{{}}', '{(})', '{()}', '{{{}[]')
for test in tests:
    print(f'{test}: {is_balanced(test)}')



def is_palindrome(s):
    sanitized = [char for char in s.lower() if char.isalnum()]
    #return sanitized == sanitized[::-1]
    return sanitized == list(reversed(sanitized))

tests = ("A man, a plan, a canal - Panama",)
for test in tests:
    print(f'{test}: {is_palindrome(test)}')



def is_anagram(s, t):
    def sanitize(s):
        return (char for char in s.lower() if char.isalnum())
    return Counter(sanitize(s)) == Counter(sanitize(t))

def is_anagram_no_counters(s, t):
    def sanitize(s):
        return [char for char in s.lower() if char.isalnum()]

    s_for_comparing = sanitize(s)
    t_for_comparing = sanitize(t)
    s_for_comparing.sort()
    t_for_comparing.sort()
    return s_for_comparing == t_for_comparing

print(is_anagram("Jim Morrison", "Mr. Mojo Risin'"))
print(is_anagram_no_counters("Jim Morrison", "Mr. Mojo Risin'"))



def reverse_list_in_place(s):
    # no s.reverse()
    start = 0
    end = len(s) - 1

    while start < end:
        temp = s[end]
        s[end] = s[start]
        s[start] = temp
        start += 1
        end -= 1

lst = ["h", "e", "l", "l", "o"]
reverse_list_in_place(lst)
print(lst)



def reverse_string(s):
    # without slicing
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

input_string = "Reverse me"
print(f'"{input_string}" reversed: {reverse_string(input_string)}')



def contains_duplicate_one_liner(nums):
    return len(set(nums)) != len(nums)

def contains_duplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate_one_liner([4, 5, 3, 2, 4]))
print(contains_duplicates([4, 5, 3, 2]))



# return list of two indexes of nums that sum to target
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
          return [num_map[complement], i]
        num_map[num] = i

assert two_sum([2, 8, 15, 4, -10, 6], 5) == [2, 4]



def reverse_int(x: int) -> int:
    x_rev = int(str(abs(x))[::-1])

    if x < 0:
        x_rev *= -1

    if x_rev < -2 ** 31 or x_rev > 2 ** 31 - 1:
        return 0
    return x_rev

print(reverse_int(5106))
print(reverse_int(-123))
print(reverse_int(0))



def first_unique_char(s):
    #c = Counter(s)
    c = my_counter(s)
    for i, char in enumerate(s):
        if c[char] == 1:
            return i
    return -1

print('index of first unique char:')
print(first_unique_char("abc"))
print(first_unique_char("abba"))
print(first_unique_char("aabbcdde"))
print(first_unique_char("aabbccbdde"))



# first letter to appear twice
def repeated_character(s):
    d = {}
    for ch in s:
        if ch in d:
            return ch
        d[ch] = None

print(f'first letter to appear twice: {repeated_character("abccbccdde")}')



def single_number(nums):
    # find the unique number where all other nums appear exactly twice
    # XOR properties:
    # XOR of a number with itself is 0.  2 ^ 2 = 0
    # XOR of a number with 0 is the number itself.  2 ^ 0 = 2
    a = 0
    for num in nums:
        a ^= num
    return a

def single_number_uses_storage(nums):
    s = set()
    for num in nums:
        try:
            s.remove(num)
        except:
            s.add(num)
    return next(iter(s))

print(single_number([1,2,3,4,3,4,1]))
print(single_number_uses_storage([1,2,3,4,3,4,1]))



# swap two numbers without temp storage and not using a, b = b, a
a = 10
b = 20
print(f'Before swap  a: {a}  b: {b}')
a = a + b
b = a - b
a = a - b
print(f'After swap   a: {a}  b: {b}')
