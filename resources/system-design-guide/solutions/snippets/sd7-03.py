from collections import OrderedDict

class LRU:
    def __init__(self, capacity):
        self.cap, self.d = capacity, OrderedDict()
    def get(self, k):
        if k not in self.d:
            return None
        self.d.move_to_end(k)            # mark most recently used
        return self.d[k]
    def put(self, k, v):
        self.d[k] = v
        self.d.move_to_end(k)
        if len(self.d) > self.cap:
            self.d.popitem(last=False)   # evict least recently used

c = LRU(2)
c.put("a", 1); c.put("b", 2)
c.get("a")                # a becomes most recent
c.put("c", 3)             # evicts b
print(c.get("a"), c.get("b"), c.get("c"))
