import threading
EPOCH = 1_600_000_000_000
class Snowflake:
    def __init__(self, worker, clock):
        self.worker, self.clock, self.last, self.seq = worker, clock, -1, 0
    def next(self):
        now = self.clock() - EPOCH
        if now < self.last: raise RuntimeError(f"clock moved backwards by {self.last - now} ms")
        if now == self.last:
            self.seq = (self.seq + 1) & 0xFFF
            if self.seq == 0:                         # sequence exhausted: wait for next millisecond
                now = self.last + 1
        else:
            self.seq = 0
        self.last = now
        return (now << 22) | (self.worker << 12) | self.seq
    @staticmethod
    def decode(i): return {"ms_since_epoch": i >> 22, "worker": (i >> 12) & 0x3FF, "seq": i & 0xFFF}
t = [EPOCH + 5000]
a, b = Snowflake(1, lambda: t[0]), Snowflake(2, lambda: t[0])
ids = [a.next() for _ in range(3)] + [b.next() for _ in range(2)]
t[0] += 1
ids += [a.next()]
print("ids:", ids)
print("decoded last:", Snowflake.decode(ids[-1]))
print("unique:", len(set(ids)) == len(ids), "| sorted by time within a worker:", ids[:3] == sorted(ids[:3]))
t[0] -= 10
try: a.next()
except RuntimeError as e: print("clock rollback handled:", e)
