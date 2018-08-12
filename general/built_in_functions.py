from datetime import datetime
from itertools import zip_longest, chain
from operator import itemgetter


# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print('print', 'example', str(9), sep='', end='\n\n')


print('enumerate() for iterating when index also needed:', list(enumerate('abc')))


# aggregate elements from iterables
lst1 = [7, 9]
lst2 = ['a', 'b', 'c']
print('zip() stops when shortest iterable exhausted:', list(zip(lst1, lst2)))
print('zip_longest() fills in with None:', list(zip_longest(lst1, lst2)))


# any and all short-circuit. any on True val, all on False val
tup = (0, False, 1, None)
print(f'any element in {tup} True? {any(tup)}')
print(f'all elements in {tup} True? {all(tup)}')


# iter, next
i = iter((False, 0, True, 'spam'))
any(i)
print('element after first True val:', next(i))


# returns range class
print('range(1, 10, 2) as list:', list(range(1, 10, 2)))


# str, repr, eval
now = datetime.now()
repr_now = repr(now)
print(f'readable: {now}  unambiguous: {repr_now}') # args converted to strings


lst = [2, 8, 3]
r = range(3, 5)
print(f'sum of {lst} and {r}: {sum(chain(lst, r))}')


lst = [9, 44, 28, 7]
prices = {'STOCK1': 10.50, 'STOCK2': 8.25, 'STOCK3': 12.45, 'STOCK4': 9.75}
print(min(lst))
print(max(44, 9))
print(f'stock ticker with lowest price: {min(prices, key=prices.get)}')
print(f'stock with highest price: {max(prices.items(), key=itemgetter(1))}')
print(f'stocks sorted by price desc: {sorted(prices.items(), key=itemgetter(1), reverse=True)}')


# returns a reverse iterator vs [::-1] which returns a list
s = 'abc'
print(f"{s} reversed: {''.join(reversed(s))}")


# filter, map mostly replaced by comprehensions
nums = [3, 9, 0, 28, 44, 1]
print(f'{nums} doubled: {list(map(lambda x: x*2, nums))}')
print(f'even vals of {nums}: {list(filter(lambda x: x % 2 == 0, nums))}')
# complementary function - itertools.filterfalse()
print(f'filter "trick" used to filter True values: {list(filter(None, nums))}')


#fromuser = input('Type something and hit Enter: ')
#print('you entered:', fromuser)
