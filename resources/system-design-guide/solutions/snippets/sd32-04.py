class LRU:
    def __init__(self, capacity_bytes): self.cap, self.used, self.items = capacity_bytes, 0, {}
    def get(self, k):
        if k in self.items: v = self.items.pop(k); self.items[k] = v; return v
    def put(self, k, size):
        if k in self.items: self.used -= self.items.pop(k)
        self.items[k] = size; self.used += size
        while self.used > self.cap:
            oldest = next(iter(self.items)); self.used -= self.items.pop(oldest)
cache = LRU(capacity_bytes=10_000_000)                     # 10 MB image cache
for name, size in [("a", 4_000_000), ("b", 4_000_000), ("c", 4_000_000)]: cache.put(name, size)
print("keys after adding three 4 MB images to a 10 MB cache:", list(cache.items), "| used:", cache.used)
cache.get("b"); cache.put("d", 3_000_000)
print("after touching b and adding d:", list(cache.items))
