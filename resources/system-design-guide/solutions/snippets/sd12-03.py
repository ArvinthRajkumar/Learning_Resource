import hashlib, math
class Bloom:
    def __init__(self, m, k):
        self.m, self.k, self.bits = m, k, bytearray(m)
    def _pos(self, item):
        for i in range(self.k):
            h = hashlib.sha256(("%d:%s" % (i, item)).encode()).digest()
            yield int.from_bytes(h[:8], "big") % self.m
    def add(self, item):
        for p in self._pos(item): self.bits[p] = 1
    def __contains__(self, item):
        return all(self.bits[p] for p in self._pos(item))

n, m = 1000, 10000
k = round(m / n * math.log(2))
b = Bloom(m, k)
for i in range(n): b.add("key%d" % i)
fp = sum(("other%d" % i) in b for i in range(10000)) / 10000
print("k =", k, "no false negatives:", all(("key%d" % i) in b for i in range(n)))
print("measured false positive rate: %.3f, theory: %.3f" % (fp, (1 - math.exp(-k * n / m)) ** k))
