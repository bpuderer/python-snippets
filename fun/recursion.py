
# divide and conquer, decrease and conquer
# reduce a problem to simpler versions of itself
# 1 or more base cases that are easy to solve. can solve directly
# each recursive call creates own frame
def mult_iter(a, b):
    result = 0
    while b > 0:    # b times
        result += a
        b -= 1
    return result


def mult_recur(a, b):
    if b == 1:
        return a
    else:
        return a + mult_recur(a, b - 1)
print(mult_recur(3, 4))



def factorial(n):
    if type(n) is not int or n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(f'5! = {factorial(5)}')



def fib(n):
   if n == 0 or n == 1:
       return 1
   else:
       return fib(n - 1) + fib(n - 2)

for n in range(5):
    print(fib(n))



def is_palindrome(s):
    def to_chars(s):
        return ''.join(c for c in s.lower() if c.isalpha())

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            # check first and last char, if False short circuits
            # [1:-1] moves in at each end one char
            return s[0] == s[-1] and is_palindrome(s[1:-1])

    return is_pal(to_chars(s))

print(is_palindrome("A man, a plan, a canal - Panama"))



def print_move(frm, to):
    print(f'move from rod {frm} to rod {to}')

def towers(num_disks, from_rod, to_rod, spare_rod):
    if num_disks == 1:
        print_move(from_rod, to_rod)
    else:
        towers(num_disks-1, from_rod, spare_rod, to_rod)
        towers(1, from_rod, to_rod, spare_rod)
        towers(num_disks-1, spare_rod, to_rod, from_rod)
towers(3, 1, 3, 2)
