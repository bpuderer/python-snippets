import heapq

class PriorityQueue:

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        # only care about value, not the associated priority
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        return str(self.elements)

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.put('abc3', 3)
    pq.put('abc2', 2)
    pq.put('abc1', 1)
    pq.put('abc2again', 2)
    pq.put('abc5', 5)
    print(pq.get())
    print(pq.get())
    print(pq)
