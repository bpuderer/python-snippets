def is_sorted(data):
    return all(data[i] <= data[i+1] for i in range(len(data) - 1))


# useless bubble sort
def bubble_sort(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
to_be_sorted = [3, 1, 10, 0, -5, 12, 11, 11, 2]
bubble_sort(to_be_sorted)
assert is_sorted(to_be_sorted)



def merge_sort(data):

    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sort(left)
        merge_sort(right)

        left_idx = 0
        right_idx = 0
        result_idx = 0

        # merge until one runs out
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                data[result_idx] = left[left_idx]
                left_idx += 1
            else:
                data[result_idx] = right[right_idx]
                right_idx += 1
            result_idx += 1

        # add (sorted) leftovers
        while left_idx < len(left):
            data[result_idx] = left[left_idx]
            left_idx += 1
            result_idx += 1

        while right_idx < len(right):
            data[result_idx] = right[right_idx]
            right_idx += 1
            result_idx += 1

to_be_sorted = [3, 1, 10, 0, -5, 12, 11, 11, 2]
merge_sort(to_be_sorted)
print(to_be_sorted)
assert is_sorted(to_be_sorted)



def selection_sort(data):
    for i in range(len(data) - 1):  # last item in the right spot
        smallest_index = i

        for j in range(i + 1, len(data)):
            if data[j] < data[smallest_index]:
                smallest_index = j

        if i != smallest_index:
            data[i], data[smallest_index] = data[smallest_index], data[i]

to_be_sorted = [3, 1, 10, 0, -5, 12, 11, 11, 2]
selection_sort(to_be_sorted)
assert is_sorted(to_be_sorted)



def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [item for item in lst if item < pivot]
    middle = [item for item in lst if item == pivot]
    right = [item for item in lst if item > pivot]
    return quicksort(left) + middle + quicksort(right)

to_be_sorted = [10, 5, 1, 12, 44, 19, 14]
sorted_lst = quicksort(to_be_sorted)
assert is_sorted(sorted_lst)
