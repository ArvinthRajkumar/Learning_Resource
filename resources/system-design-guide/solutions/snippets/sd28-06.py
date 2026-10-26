class GCounter:
    def __init__(self, rid): self.rid, self.counts = rid, {}
    def inc(self, n=1): self.counts[self.rid] = self.counts.get(self.rid, 0) + n
    def value(self): return sum(self.counts.values())
    def merge(self, other):
        for k, v in other.counts.items(): self.counts[k] = max(self.counts.get(k, 0), v)
a, b, c = GCounter("a"), GCounter("b"), GCounter("c")
a.inc(3); b.inc(2); c.inc(4)
# merge in different orders, with a duplicate delivery: all replicas converge
x, y = GCounter("x"), GCounter("y")
for r in (a, b, c, a): x.merge(r)
for r in (c, a, b): y.merge(r)
print("replica x:", x.value(), "| replica y:", y.value(), "| identical state:", x.counts == y.counts)
class ORSet:
    def __init__(self, rid): self.rid, self.n, self.adds, self.removed = rid, 0, set(), set()
    def add(self, e): self.n += 1; self.adds.add((e, f"{self.rid}{self.n}"))
    def remove(self, e): self.removed |= {t for t in self.adds if t[0] == e}
    def elements(self): return sorted({e for e, tag in self.adds if (e, tag) not in self.removed})
    def merge(self, o): self.adds |= o.adds; self.removed |= o.removed
p, q = ORSet("p"), ORSet("q")
p.add("milk"); q.merge(p)                      # both see milk
p.remove("milk"); q.add("milk")                # concurrent: p removes the old milk, q adds a new milk
p.merge(q); q.merge(p)
print("concurrent remove and add -> add wins on both replicas:", p.elements(), q.elements())
