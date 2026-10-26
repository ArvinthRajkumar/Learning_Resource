import json
class TinyDB:
    """Key-value store with a write-ahead log; the 'disk page' may be lost in a crash."""
    def __init__(self): self.log, self.pages = [], {}
    def put(self, k, v):
        self.log.append(json.dumps({"op": "put", "k": k, "v": v}))   # 1. log first (fsync)
        self.pages[k] = v                                                # 2. page later (may be lost)
    def crash(self): self.pages = {}                                     # in-memory state vanishes
    def recover(self):
        for line in self.log:
            r = json.loads(line)
            if r["op"] == "put": self.pages[r["k"]] = r["v"]
db = TinyDB()
db.put("a", 1); db.put("b", 2); db.put("a", 3)
db.crash()
print("after crash:", db.pages)
db.recover()
print("after replaying the log:", db.pages)
