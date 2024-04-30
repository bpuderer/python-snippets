class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        #return len(self.items) == 0
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def reverse_string(my_string):
    s = Stack()
    for ch in my_string:
        s.push(ch)
    reversed_str = ''
    while not s.is_empty():
        reversed_str += s.pop()
    return reversed_str


if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print(s.pop())
    print(s)

    print(reverse_string('abcdefg'))
