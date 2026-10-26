import threading
class Counter:
    def __init__(self):
        self._n, self._lock = 0, threading.Lock()
    def incr(self):
        with self._lock:
            self._n += 1
    @property
    def value(self): return self._n
c = Counter()
ts = [threading.Thread(target=lambda: [c.incr() for _ in range(5000)]) for _ in range(4)]
[t.start() for t in ts]; [t.join() for t in ts]
print(c.value)
