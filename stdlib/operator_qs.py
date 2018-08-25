import operator


# use operator module instead of redefining an intrinsic python operator using lambda
# https://docs.python.org/3/library/operator.html#mapping-operators-to-functions

numbers = [9, 4, 17]
#print([-num for num in numbers])
print(list(map(operator.neg, numbers)))


# itemgetter. can specify multiple items
lst = [{'a': 2001}, {'a': 0}, {'a': 2112}, {'a': 2010}]
print(lst)
lst.sort(key=operator.itemgetter('a'))
print('sorted on value of "a":', lst)

lst = [(1, 2112), (0, 2001), (2, 2010)]
print(lst)
lst.sort(key=operator.itemgetter(1))
print('sorted on second item in tuple:', lst)



# attrgetter. can specify multiple attributes
class MyClass:
    def __init__(self, val):
        self.val = val

    def inc_val(self):
        self.val += 1

    def is_even(self):
        return self.val % 2 == 0

lst = [MyClass(2112), MyClass(2010), MyClass(2001)]
print([o.val for o in lst])
lst.sort(key=operator.attrgetter('val'))
print('sorted on val attrib:', [o.val for o in lst])


# methodcaller
print('all even?', all(map(operator.methodcaller('is_even'), lst)))
print('any even?', any(map(operator.methodcaller('is_even'), lst)))
