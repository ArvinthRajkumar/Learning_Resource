from collections import defaultdict, OrderedDict

class LFU:
    def __init__(self, capacity):
        self.cap, self.min_count = capacity, 0
        self.kv = {}                                        # key -> (value, count)
        self.buckets = defaultdict(OrderedDict)             # count -> ordered keys (oldest first)
    def _touch(self, key):
        value, c = self.kv[key]
        del self.buckets[c][key]
        if not self.buckets[c]:
            del self.buckets[c]
            if self.min_count == c:
                self.min_count += 1
        self.kv[key] = (value, c + 1)
        self.buckets[c + 1][key] = None
    def get(self, key):
        if key not in self.kv: return -1
        self._touch(key)
        return self.kv[key][0]
    def put(self, key, value):
        if self.cap == 0: return
        if key in self.kv:
            self.kv[key] = (value, self.kv[key][1])
            self._touch(key)
            return
        if len(self.kv) >= self.cap:
            victim, _ = self.buckets[self.min_count].popitem(last=False)
            if not self.buckets[self.min_count]:
                del self.buckets[self.min_count]
            del self.kv[victim]
        self.kv[key] = (value, 1)
        self.buckets[1][key] = None
        self.min_count = 1

c = LFU(2)
c.put(1, 1); c.put(2, 2)
print(c.get(1))        # 1, key 1 now used twice
c.put(3, 3)            # evicts key 2 (least frequently used)
print(c.get(2), c.get(3))
c.put(4, 4)            # keys 1 and 3 both have count 2, so the less recently used key 1 is evicted
print(c.get(1), c.get(3), c.get(4))
