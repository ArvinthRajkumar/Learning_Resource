from collections import deque, namedtuple, OrderedDict
import heapq
q = deque([1, 2, 3], maxlen=3)
q.append(4); q.appendleft(0)
print(q)
Point = namedtuple("Point", "x y")
p = Point(1, 2)
print(p, p.x, p._replace(y=9))
h = [5, 1, 4]
heapq.heapify(h)
heapq.heappush(h, 0)
print([heapq.heappop(h) for _ in range(4)], heapq.nlargest(2, [4, 9, 1, 7]))
