import bisect, random
random.seed(0)
class BPlusTree:
    """Tiny B+tree with insert and range scan (order = max keys per node)."""
    def __init__(self, order=4):
        self.order, self.root = order, {"leaf": True, "keys": [], "vals": [], "next": None}
        self.splits = 0
    def _find_leaf(self, node, k):
        while not node["leaf"]:
            node = node["kids"][bisect.bisect_right(node["keys"], k)]
        return node
    def insert(self, k, v):
        split = self._insert(self.root, k, v)
        if split:
            sep, right = split
            self.root = {"leaf": False, "keys": [sep], "kids": [self.root, right]}
    def _insert(self, node, k, v):
        if node["leaf"]:
            i = bisect.bisect_left(node["keys"], k)
            if i < len(node["keys"]) and node["keys"][i] == k: node["vals"][i] = v; return None
            node["keys"].insert(i, k); node["vals"].insert(i, v)
            if len(node["keys"]) <= self.order: return None
            mid = len(node["keys"]) // 2
            right = {"leaf": True, "keys": node["keys"][mid:], "vals": node["vals"][mid:], "next": node["next"]}
            node["keys"], node["vals"], node["next"] = node["keys"][:mid], node["vals"][:mid], right
            self.splits += 1
            return right["keys"][0], right
        i = bisect.bisect_right(node["keys"], k)
        res = self._insert(node["kids"][i], k, v)
        if not res: return None
        sep, right = res
        node["keys"].insert(i, sep); node["kids"].insert(i + 1, right)
        if len(node["keys"]) <= self.order: return None
        mid = len(node["keys"]) // 2
        up = node["keys"][mid]
        right = {"leaf": False, "keys": node["keys"][mid + 1:], "kids": node["kids"][mid + 1:]}
        node["keys"], node["kids"] = node["keys"][:mid], node["kids"][:mid + 1]
        self.splits += 1
        return up, right
    def get(self, k):
        leaf = self._find_leaf(self.root, k)
        i = bisect.bisect_left(leaf["keys"], k)
        return leaf["vals"][i] if i < len(leaf["keys"]) and leaf["keys"][i] == k else None
    def scan(self, lo, hi):
        leaf, out = self._find_leaf(self.root, lo), []
        while leaf:
            for k, v in zip(leaf["keys"], leaf["vals"]):
                if k > hi: return out
                if k >= lo: out.append(k)
            leaf = leaf["next"]
        return out
    def height(self):
        h, n = 1, self.root
        while not n["leaf"]: n = n["kids"][0]; h += 1
        return h
keys = random.sample(range(100000), 5000)
t = BPlusTree(order=8)
for k in keys: t.insert(k, k * 2)
assert all(t.get(k) == k * 2 for k in keys[:500]) and t.get(-5) is None
assert t.scan(1000, 2000) == sorted(k for k in keys if 1000 <= k <= 2000)
print("5000 keys, order 8: height", t.height(), "| node splits", t.splits, "| point lookups and range scan verified")
