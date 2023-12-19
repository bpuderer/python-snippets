from collections import OrderedDict, Counter


# remove duplicates from sequence while preserving order
# https://stackoverflow.com/a/7961425    Raymond Hettinger
lst = [4, 1, 2, 1, 3, 3, 2, 4]
print("with duplicates removed, order maintained:", list(OrderedDict.fromkeys(lst)))



# remove duplicates from sorted list in place. non-decreasing order.  easy, start from end.
def remove_duplicates_in_place(nums):
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i]

nums = [0, 0, 1, 2, 2, 2, 2, 2, 4, 4, 4]
remove_duplicates_in_place(nums)
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



def reverse_int(x: int) -> int:
    x_rev = int(str(abs(x))[::-1])

    if x < 0:
        x_rev *= -1

    if x_rev <= -2 ** 31 or x_rev >= 2 ** 31 - 1:
        return 0
    return x_rev

print(reverse_int(5106))
print(reverse_int(-123))
print(reverse_int(0))



def first_unique_char(s):
    c = Counter(s)
    for i, char in enumerate(s):
        if c[char] == 1:
            return i
    return -1

print('index of first unique char:')
print(first_unique_char("abc"))
print(first_unique_char("aabb"))
print(first_unique_char("aabbcdde"))
print(first_unique_char("aabbccdde"))



def single_number(nums):
    # all other nums in list appear exactly twice
    # 2 ^ 2 = 0
    # 2 ^ 0 = 2
    # true only if args differ
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
