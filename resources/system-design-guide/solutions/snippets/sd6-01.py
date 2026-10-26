# A grow-only counter CRDT (G-Counter): each node counts only its own increments.
# Merging takes the per-node maximum, so merges are order independent and repeatable.
class GCounter:
    def __init__(self, node):
        self.node, self.counts = node, {}
    def incr(self, n=1):
        self.counts[self.node] = self.counts.get(self.node, 0) + n
    def value(self):
        return sum(self.counts.values())
    def merge(self, other):
        for k, v in other.counts.items():
            self.counts[k] = max(self.counts.get(k, 0), v)

a, b = GCounter("A"), GCounter("B")
a.incr(3); b.incr(2)          # concurrent updates on two replicas
a.merge(b); b.merge(a)        # gossip in any order, any number of times
b.merge(a)
print(a.value(), b.value())   # both converge to 5
