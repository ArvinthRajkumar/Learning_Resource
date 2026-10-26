import threading
from collections import OrderedDict

class ThreadSafeLRU:
    def __init__(self, capacity, on_evict=None):
        self.cap, self.d, self.lock, self.on_evict = capacity, OrderedDict(), threading.Lock(), on_evict
    def get(self, k):
        with self.lock:
            if k not in self.d: return None
            self.d.move_to_end(k)
            return self.d[k]
    def put(self, k, v):
        with self.lock:
            self.d[k] = v
            self.d.move_to_end(k)
            if len(self.d) > self.cap:
                old = self.d.popitem(last=False)
                if self.on_evict: self.on_evict(*old)

evicted = []
c = ThreadSafeLRU(2, on_evict=lambda k, v: evicted.append(k))
for i in range(5):
    c.put(i, i)
print(list(c.d), evicted)
