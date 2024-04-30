from collections import deque


def print_binary_numbers_1_to_n(n):
    if n <= 0:
        return
    q = deque()
    q.append(1)

    for i in range(n):
        binary = q.popleft()
        print(binary)
        q.append(binary * 10)
        q.append(binary * 10 + 1)


print_binary_numbers_1_to_n(10)
