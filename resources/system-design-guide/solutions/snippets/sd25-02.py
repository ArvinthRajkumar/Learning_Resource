class LockService:
    def __init__(self): self.token, self.holder, self.expires = 0, None, 0
    def acquire(self, client, now, lease):
        if self.holder is None or now >= self.expires:
            self.token += 1
            self.holder, self.expires = client, now + lease
            return self.token
        return None
class Storage:
    def __init__(self): self.max_token, self.value = 0, None
    def write(self, token, value):
        if token < self.max_token: return f"REJECTED stale token {token} (seen {self.max_token})"
        self.max_token, self.value = token, value
        return f"accepted token {token}"
lock, store = LockService(), Storage()
t1 = lock.acquire("A", now=0, lease=10)
print("A acquires, token", t1)
print("A pauses (GC) past its lease; B acquires at t=15:", lock.acquire("B", now=15, lease=10))
t2 = lock.token
print("B writes:", store.write(t2, "from B"))
print("A wakes up and writes with its old token:", store.write(t1, "from A (zombie)"))
print("final value:", store.value)
