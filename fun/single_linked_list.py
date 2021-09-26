class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.node_count = 0

    def __str__(self):
        curr = self.head
        temp = []
        while curr is not None:
            temp.append(str(curr.data))
            curr = curr.next
        temp.append(str(None))
        return " -> ".join(temp)

    def insert_at_beginning(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            # set head to new node
            temp.next = self.head
            self.head = temp
        self.node_count += 1

    def insert_at_end(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            # set next of last item to new node
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = temp
        self.node_count += 1

    def insert_at_given_position(self, data, position):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        elif position <= 1:
            self.insert_at_beginning(data)
        elif position > self.node_count:
            self.insert_at_end(data)
        else:
            count = 1
            curr = self.head
            while count < position - 1:  # inserting after
                curr = curr.next
                count += 1
            temp.next = curr.next
            curr.next = temp
        self.node_count += 1

    def delete_from_beginning(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            del temp
            self.node_count -= 1

    def delete_from_end(self):
        if self.head is not None:
            if self.head.next is None:
                self.delete_from_beginning()
            else:
                # need reference to last and next to last.  delete last and update next of the next to last to None
                curr = self.head
                prev = None
                while curr.next is not None:    # 1 item list falls through here immediately
                    prev = curr
                    curr = curr.next
                prev.next = None                # does not work on one item list, prev = None
                del curr
            self.node_count -= 1

    def delete_at_position(self, position):
        if self.head is not None:
            if position <= 1:
                self.delete_from_beginning()
            elif position >= self.node_count:
                self.delete_from_end()
            else:
                curr = self.head
                prev = None
                count = 1
                while count < position:
                    prev = curr
                    curr = curr.next
                    count += 1
                prev.next = curr.next
                del curr
            self.node_count -= 1



# simple demo
list1 = LinkedList()
print(list1)
list1.insert_at_beginning(5)
list1.insert_at_beginning(6)
list1.insert_at_end(7)
list1.insert_at_end(8)
list1.insert_at_given_position(1, 1)
list1.insert_at_given_position(3, 4)
print(list1)
list1.delete_from_beginning()
list1.delete_from_end()
list1.delete_at_position(2)
print(list1)

