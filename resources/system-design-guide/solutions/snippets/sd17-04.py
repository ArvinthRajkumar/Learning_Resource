class Elevator:
    def __init__(self, floor=0):
        self.floor, self.dir, self.up, self.down = floor, 0, set(), set()
    def request(self, f):
        (self.up if f >= self.floor else self.down).add(f)
    def step(self):
        """Move one floor along SCAN order and return the floor visited."""
        if self.dir >= 0 and any(f >= self.floor for f in self.up):
            self.dir = 1
        elif self.down:
            self.dir = -1
        elif self.up:
            self.dir = 1
        else:
            self.dir = 0
            return None
        self.floor += self.dir
        self.up.discard(self.floor); self.down.discard(self.floor)
        return self.floor

e = Elevator(0)
for f in (3, 5, 2): e.request(f)
trace = []
for _ in range(7):
    trace.append(e.step())
print(trace)
