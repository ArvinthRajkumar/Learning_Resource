from collections import deque
import heapq

class CircularQueue:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.front = self.size = 0
        self.cap = capacity

    def enqueue(self, x):
        if self.size == self.cap:
            return False                       # full
        self.data[(self.front + self.size) % self.cap] = x
        self.size += 1
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.front]
        self.front = (self.front + 1) % self.cap    # wrap around
        self.size -= 1
        return x

q = deque([1, 2, 3])
q.append(4); q.appendleft(0); q.popleft()
pq = []
for x in (5, 1, 3):
    heapq.heappush(pq, x)
smallest = heapq.heappop(pq)
