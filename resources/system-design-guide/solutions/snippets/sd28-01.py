class Node:
    def __init__(self, name): self.name, self.t, self.log = name, 0, []
    def event(self, what):
        self.t += 1; self.log.append((self.t, self.name, what)); return self.t
    def send(self, what):
        self.t += 1; self.log.append((self.t, self.name, "send " + what)); return self.t
    def receive(self, stamp, what):
        self.t = max(self.t, stamp) + 1; self.log.append((self.t, self.name, "recv " + what))
a, b, c = Node("A"), Node("B"), Node("C")
a.event("start"); s = a.send("m1"); b.event("local"); b.receive(s, "m1")
s2 = b.send("m2"); c.event("local"); c.receive(s2, "m2")
for line in sorted(a.log + b.log + c.log): print(line)
