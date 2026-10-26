import bisect, hashlib

class Ring:
    def __init__(self, nodes=(), vnodes=100):
        self.vnodes = vnodes
        self.keys = []      # sorted hash positions
        self.owner = {}     # position -> node
        for n in nodes:
            self.add(n)

    @staticmethod
    def _h(s):
        return int(hashlib.md5(s.encode()).hexdigest(), 16)

    def add(self, node):
        for i in range(self.vnodes):
            p = self._h("%s#%d" % (node, i))
            bisect.insort(self.keys, p)
            self.owner[p] = node

    def remove(self, node):
        for i in range(self.vnodes):
            p = self._h("%s#%d" % (node, i))
            self.keys.remove(p)
            del self.owner[p]

    def get(self, key):
        i = bisect.bisect(self.keys, self._h(key)) % len(self.keys)
        return self.owner[self.keys[i]]

keys = ["user%d" % i for i in range(10000)]
ring = Ring(["A", "B", "C", "D"])
before = {k: ring.get(k) for k in keys}
ring.add("E")
after = {k: ring.get(k) for k in keys}
moved = sum(1 for k in keys if before[k] != after[k])
print("keys moved after adding a 5th node: %.1f%% (ideal 20%%)" % (100 * moved / len(keys)))
counts = {}
for k in keys:
    counts[after[k]] = counts.get(after[k], 0) + 1
print(sorted(counts.items()))
