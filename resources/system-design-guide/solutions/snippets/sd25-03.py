import heapq
class Scheduler:
    def __init__(self): self.heap, self.log = [], []
    def add(self, run_at, name, every=None): heapq.heappush(self.heap, (run_at, name, every))
    def run_until(self, now):
        while self.heap and self.heap[0][0] <= now:
            t, name, every = heapq.heappop(self.heap)
            self.log.append((t, name))
            if every: heapq.heappush(self.heap, (t + every, name, every))      # reschedule cron-like job
s = Scheduler()
s.add(5, "report", every=10); s.add(7, "email"); s.add(12, "cleanup")
s.run_until(30)
print(s.log)
