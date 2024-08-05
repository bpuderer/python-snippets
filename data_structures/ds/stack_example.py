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


def reverse_string(s):
    stack = list(s)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str

TEST_STR = 'abc123'
print(f'{TEST_STR} reversed is {reverse_string(TEST_STR)}')
