import time

class Cache:
    def __init__(self):
        self.d = {}
    def get(self, k):
        v = self.d.get(k)
        if v and v[1] > time.monotonic():
            return v[0]
        self.d.pop(k, None)
        return None
    def set(self, k, val, ttl):
        self.d[k] = (val, time.monotonic() + ttl)
    def delete(self, k):
        self.d.pop(k, None)

db = {"user:1": "Ada"}
db_reads = [0]
cache = Cache()

def get_user(k):
    v = cache.get(k)
    if v is not None:
        return v
    db_reads[0] += 1                 # slow path
    v = db[k]
    cache.set(k, v, ttl=60)
    return v

def update_user(k, v):
    db[k] = v
    cache.delete(k)                  # invalidate, do not update

for _ in range(5): get_user("user:1")
update_user("user:1", "Grace")
print(get_user("user:1"), "db reads:", db_reads[0])
