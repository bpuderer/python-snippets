import operator


lst = []
lst.append('b')     # add to end
lst.extend('cde')   # appends items from iterable
lst.insert(0, 'a')  # add at index
print(lst)
print(lst.pop())    # remove from end
print(lst)
lst.pop(0)          # remove from beginning
print(lst)


# 2D
lst2 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
for i, row in enumerate(lst2):
    for j, element in enumerate(row):
        print(f'({i}, {j}): {element}')


# sorted, sort.  sorted returns a new list.  sort mutates the list
grades = [("Beth", 95), ("Abe", 89), ("Beth", 88), ("Claire", 92)]
print(sorted(grades))   # uses first item in tuple for sorting, then second...
print(sorted(grades, key=lambda x: x[1], reverse=False))
print(sorted(grades, key=operator.itemgetter(1), reverse=True))
grades.sort(key=operator.itemgetter(1))
print(grades)


def find_second_smallest(my_list):
    # assume no duplicates
    if len(my_list) < 2:
        return None

    #return sorted(my_list)[1]
    #return sorted(set(my_list))[1]

    # or math.inf
    smallest = float('inf')
    second_smallest = float('inf')

    for num in my_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest


print(find_second_smallest([5, 8, 3, 2, 6]))
print(find_second_smallest([1, 8, 9, 7, 6]))
print(find_second_smallest([5, 4]))
print(find_second_smallest([4, 5]))
