from collections import deque

d = deque()

# as a queue.  FIFO.  enqueue, dequeue
d.append("a")
d.append("b")
d.append("c")
print(d)
while len(d) > 0:
    item = d.popleft()
    print(item)
