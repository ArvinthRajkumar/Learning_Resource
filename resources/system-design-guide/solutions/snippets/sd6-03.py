class Lamport:
    def __init__(self): self.t = 0
    def event(self): self.t += 1; return self.t
    def send(self): return self.event()
    def recv(self, ts): self.t = max(self.t, ts) + 1; return self.t

a, b = Lamport(), Lamport()
a.event(); a.event()
ts = a.send()
print("A sends with", ts, "-> B local time after receive:", b.recv(ts))
