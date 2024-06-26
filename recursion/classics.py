import sys
# https://pythontutor.com/python-compiler.html#mode=edit

print(f'Recursion limit: {sys.getrecursionlimit()}')


def factorial_iterative(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
       return 1

    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def factorial(n):
    if n < 0:
        return None
    if n == 0:
       return 1
    else:
        return n * factorial(n - 1)

assert factorial_iterative(6) == 720
assert factorial_iterative(1) == 1
assert factorial_iterative(0) == 1
assert factorial_iterative(-7) == None

assert factorial(6) == 720
assert factorial(1) == 1
assert factorial(0) == 1
assert factorial(-7) == None



#nth fib number
def fib_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fib_recursive(n):
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

assert fib_iterative(7) == 13
assert fib_recursive(7) == 13



def sum_num_sequence_iterative(lst):
    sum = 0
    for item in lst:
        sum += item
    return sum

def sum_num_sequence_recursive(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_num_sequence_recursive(lst[1:])

assert sum_num_sequence_iterative([1, 4, 12, -50, 100]) == 67
assert sum_num_sequence_recursive([1, 4, 12, -50, 100]) == 67



def sum_list_numbers_mult_by_depth(lst, initial_depth=1):
    result = 0
    for num in lst:
        if isinstance(num, list):
            result += sum_list_numbers_mult_by_depth(num, initial_depth=initial_depth+1)
        else:
            result += num * initial_depth
            print(num, initial_depth)
    return result

assert sum_list_numbers_mult_by_depth([]) == 0
assert sum_list_numbers_mult_by_depth([1, 2, 3]) == 6
assert sum_list_numbers_mult_by_depth([1, 2, 3, [100]]) == 206
assert sum_list_numbers_mult_by_depth([1, [100], [101]]) == 403
assert sum_list_numbers_mult_by_depth([1, [10], [[20], [20], [[30, [40, 45]]]]]) == 686



def mult_num_sequence_recursive(lst):
    if len(lst) == 0:
        return 1
    return lst[0] * mult_num_sequence_recursive(lst[1:])
assert mult_num_sequence_recursive([3, 4, 2, -1]) == -24



def mult_recur(a, b):
    if a == 0 or b == 0:
        return 0
    if b < 0:
        b = abs(b)
        a = -a
    if b == 1:
        return a
    else:
        return a + mult_recur(a, b - 1)

assert mult_recur(3, -4) == -12
assert mult_recur(-3, 4) == -12
assert mult_recur(3, 4) == 12



def exp_recur(n, pow):
    # assumes pow is >= 0
    if pow == 0:
        return 1
    else:
        return n * exp_recur(n, pow - 1)

assert exp_recur(2, 5) == 32
assert exp_recur(-2, 5) == -32
assert exp_recur(5, 3) == 125



def str_len_recur(string):
    if not string:  # string == ''
        return 0
    else:
        return 1 + str_len_recur(string[1:])

assert str_len_recur("abcxyz") == 6



def max_value(data):
    if len(data) == 1:
        return data[0]
    else:
        val1 = data[0]
        val2 = max_value(data[1:])

        if val1 > val2:
            return val1
        else:
            return val2

data = [12, 13, 0, -3, -3, 12, 15, 7, 2]
assert max_value(data) == 15



def gcd_iter(a, b):
    while b:     # b != 0
        a, b = b, a % b
    return a

assert gcd_iter(28, 16) == 4
assert gcd_iter(16, 28) == 4
assert gcd_iter(17, 5) == 1
assert gcd_iter(5, 31) == 1

def gcd_recur(a, b):
    # GCD(a, b) = GCD(b, a-b)
    # GCD(a, b) = GCD(b, a % b)
    # https://en.wikipedia.org/wiki/Euclidean_algorithm
    if b == 0:
        return a
    else:
        return gcd_recur(b, a % b)

assert gcd_recur(28, 16) == 4
assert gcd_recur(16, 28) == 4
assert gcd_recur(17, 5) == 1
assert gcd_recur(5, 31) == 1



def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [item for item in lst if item < pivot]
    middle = [item for item in lst if item == pivot]
    right = [item for item in lst if item > pivot]
    return quicksort(left) + middle + quicksort(right)

assert quicksort([10, 5, 1, 12, 44, 19, 14]) == [1, 5, 10, 12, 14, 19, 44]



def cleanup_str(s):
        return ''.join(c for c in s.lower() if c.isalpha())

def is_palindrome(s):
        if len(s) <= 1:
            return True
        else:
            # check first and last char, if False short circuits
            # [1:-1] moves in at each end one char
            # remember [1:-1] is the second to second to last since the -1 is not inclusive
            return s[0] == s[-1] and is_palindrome(s[1:-1])

assert is_palindrome(cleanup_str("A man, a plan, a canal - Panama"))
assert is_palindrome(cleanup_str("motor")) == False
assert is_palindrome(cleanup_str("rotor"))



def towers(n, source, destination, spare):
    if n == 1:
        print(f'move disk 1 from rod {source} to rod {destination}')
        return
    towers(n - 1, source, spare, destination)
    print(f'move disk {n} from rod {source} to rod {destination}')
    towers(n - 1, spare, destination, source)

NUM_DISCS = 3
towers(NUM_DISCS,'A', 'C', 'B')
