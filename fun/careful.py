# http://pythontutor.com/
from itertools import zip_longest


print('CLASSIC GOTCHA: Mutable default args')
def append_to(element, lst=[]):
    lst.append(element)
    return lst

print('append_to(42):', append_to(42))
print('append_to(2112):', append_to(2112))
print('Why is 42 from previous call included? Default args only evaluated when defined')

print('--')

print('Typical solution')
def append_to_fixed(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst

print(append_to_fixed(42))
print(append_to_fixed(2112))


print('-----')


print('zip() short circuits')
vals1 = [1, 2, 3]
vals2 = [1]
print(f'vals1: {vals1} vals2: {vals2}  list(zip(vals1, vals2)): {list(zip(vals1, vals2))}')

print('--')

print('use itertools.zip_longest() to fill in missing with None')
print(f'vals1: {vals1} vals2: {vals2}  list(zip_longest(vals1, vals2)): {list(zip_longest(vals1, vals2))}')


print('-----')


print('one item tuples need a trailing comma')
print(f'(3) {type((3))}\n(3,) {type((3,))}')


print('-----')


print('Initialize 2-D matrix')
board = [[0]*4]*4
board[0][0] = 42
print('setting [0][0] to 42...')
print(board)
print('Uh oh. [0] on each row set.  Why?  Each row references the same list')

print('--')

# better
board = [[0]*4 for _ in range(4)]
#board = [[0 for _ in range(4)] for _ in range(4)]
board[0][0] = 42
print(board)


print('-----')


x = []
y = x
x.append(1)
print(x)
print(y)
print('Why does y have the 1 when it was added to x? ASSIGNMENT **DOES NOT** COPY!')


print('-----')


# https://stackoverflow.com/a/4845327
print('+= looks for __iadd__, + looks for __add__')
x = []
print(f'x: {x}        id(x): {id(x)}')
x += [1]
print(f'After x += [1]\nx:    {x}    id(x): {id(x)}')
x = x + [2]
print(f'After x = x + [2]\nx: {x}    id(x): {id(x)}')


print('-----')


# https://docs.python.org/3/reference/expressions.html#generator-expressions
# https://www.python.org/dev/peps/pep-0289/#early-binding-versus-late-binding
# "the first (outermost) for-expression should be evaluated immediately and that the remaining
# expressions be evaluated when the generator is executed."
print("Early/late binding for generator expressions")
lst1 = [0, 1]
lst2 = [999, 999]
g = (i+j for i in lst1 for j in lst2)
lst1 = [999, 999]
lst2 = [100, 200]
print(list(g))
