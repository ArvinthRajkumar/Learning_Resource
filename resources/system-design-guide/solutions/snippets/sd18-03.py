import bisect
class LSM:
    def __init__(self, memtable_limit=4):
        self.mem, self.limit, self.tables, self.reads_touched = {}, memtable_limit, [], 0
    def put(self, k, v):
        self.mem[k] = v
        if len(self.mem) >= self.limit: self.flush()
    def delete(self, k): self.put(k, None)             # tombstone
    def flush(self):
        self.tables.insert(0, sorted(self.mem.items()))  # newest first
        self.mem = {}
    def get(self, k):
        if k in self.mem: return self.mem[k]
        for t in self.tables:
            self.reads_touched += 1
            i = bisect.bisect_left(t, (k,))
            if i < len(t) and t[i][0] == k: return t[i][1]
        return None
    def compact(self):
        merged = {}
        for t in reversed(self.tables):                  # oldest first, newer overwrites
            merged.update(dict(t))
        self.tables = [sorted((k, v) for k, v in merged.items() if v is not None)]
db = LSM()
for i in range(10): db.put(f"k{i}", i)
db.put("k3", 333); db.delete("k5")
for i in range(10, 14): db.put(f"k{i}", i)
print("sstables before compaction:", len(db.tables))
print("k3 =", db.get("k3"), "| k5 (deleted) =", db.get("k5"), "| k0 =", db.get("k0"), "| sstables touched so far:", db.reads_touched)
db.compact()
print("sstables after compaction:", len(db.tables), "| entries:", len(db.tables[0]), "| k3 =", db.get("k3"), "| k5 =", db.get("k5"))
