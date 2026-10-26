import heapq, bisect
from collections import Counter, defaultdict, deque, OrderedDict, namedtuple, ChainMap
words = "to be or not to be that is the question to".split()
c = Counter(words)
print("most common:", c.most_common(2), "| total:", sum(c.values()), "| c['be']:", c["be"], "| missing:", c["xyz"])
groups = defaultdict(list)
for w in words: groups[len(w)].append(w)
print("by length:", dict(groups))
dq = deque(maxlen=3)
for i in range(6): dq.append(i)
print("bounded deque keeps last three:", list(dq))
heap = [5, 1, 8, 3, 2]
heapq.heapify(heap)
print("heap pops in order:", [heapq.heappop(heap) for _ in range(3)], "| nlargest:", heapq.nlargest(2, [5, 1, 8, 3, 2]))
scores = [10, 20, 30, 40]
print("bisect insertion index for 25:", bisect.bisect(scores, 25), "| keeps list sorted:", (bisect.insort(scores, 25), scores)[1])
Point = namedtuple("Point", "x y")
p = Point(3, 4)
print(p, p.x, p._asdict(), "| ChainMap lookup:", ChainMap({"a": 1}, {"a": 2, "b": 3})["b"])
