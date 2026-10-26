import time
EPOCH = 1_700_000_000_000
class Snowflake:
    def __init__(self, machine):
        self.machine, self.last, self.seq = machine, -1, 0
    def next(self, now_ms=None):
        now = now_ms if now_ms is not None else int(time.time() * 1000)
        if now == self.last:
            self.seq = (self.seq + 1) & 0xFFF
            if self.seq == 0:
                raise RuntimeError("sequence exhausted this millisecond")
        else:
            self.seq, self.last = 0, now
        return ((now - EPOCH) << 22) | (self.machine << 12) | self.seq

g = Snowflake(machine=5)
ids = [g.next(EPOCH + 1000) for _ in range(3)] + [g.next(EPOCH + 1001)]
print(ids, ids == sorted(ids))
print("timestamp bits:", ids[0] >> 22, "machine:", (ids[0] >> 12) & 0x3FF, "seq:", ids[0] & 0xFFF)
