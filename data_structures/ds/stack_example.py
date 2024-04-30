# matching parens
def has_matching_parens(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(has_matching_parens("(abc())"))
print(has_matching_parens("(abc(())("))


def reverse_string(string):
    s = []
    result = ''
    for ch in string:
        s.append(ch)
    while s:
        result += s.pop()
    return result

TEST_STR = 'abc123'
print(f'{TEST_STR} reversed is {reverse_string(TEST_STR)}')
