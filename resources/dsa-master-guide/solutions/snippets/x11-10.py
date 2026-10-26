import threading, collections
class BoundedQueue:
    def __init__(self, capacity):
        self.cap, self.q = capacity, collections.deque()
        self.lock = threading.Lock()
        self.not_full, self.not_empty = threading.Condition(self.lock), threading.Condition(self.lock)
    def put(self, item):
        with self.not_full:
            while len(self.q) >= self.cap: self.not_full.wait()
            self.q.append(item); self.not_empty.notify()
    def get(self):
        with self.not_empty:
            while not self.q: self.not_empty.wait()
            item = self.q.popleft(); self.not_full.notify(); return item
q, produced, consumed = BoundedQueue(3), list(range(200)), []
def producer():
    for x in produced: q.put(x)
def consumer():
    for _ in range(len(produced)): consumed.append(q.get())
threads = [threading.Thread(target=producer), threading.Thread(target=consumer)]
for t in threads: t.start()
for t in threads: t.join()
print("all items arrived in order through a queue of capacity 3:", consumed == produced, "| never exceeded capacity:", len(q.q) <= 3)
