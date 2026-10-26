from collections import OrderedDict
class LRU:
    def __init__(self, cap): self.cap, self.d = cap, OrderedDict()
    def get(self, k):
        if k not in self.d: return -1
        self.d.move_to_end(k); return self.d[k]
    def put(self, k, v):
        self.d[k] = v; self.d.move_to_end(k)
        if len(self.d) > self.cap: self.d.popitem(last=False)
c = LRU(2)
c.put(1, 1); c.put(2, 2); assert c.get(1) == 1
c.put(3, 3); assert c.get(2) == -1
c.put(4, 4); assert c.get(1) == -1 and c.get(3) == 3 and c.get(4) == 4
def flatten(x):
    stack = [iter(x)]
    while stack:
        for item in stack[-1]:
            if isinstance(item, list): stack.append(iter(item)); break
            yield item
        else:
            stack.pop()
print("LRU behaves; flatten:", list(flatten([1, [2, [3, [4]], 5], [], [[6]]])))
