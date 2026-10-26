import hashlib, math
class Bloom:
    def __init__(self, m, k): self.m, self.k, self.bits = m, k, bytearray(m)
    def _hashes(self, x):
        for i in range(self.k):
            yield int(hashlib.sha256(f"{i}:{x}".encode()).hexdigest(), 16) % self.m
    def add(self, x):
        for h in self._hashes(x): self.bits[h] = 1
    def __contains__(self, x): return all(self.bits[h] for h in self._hashes(x))
n, m, k = 5000, 50000, 7
b = Bloom(m, k)
for i in range(n): b.add(f"user{i}")
assert all(f"user{i}" in b for i in range(n))                     # no false negatives
fp = sum(f"other{i}" in b for i in range(20000)) / 20000
theory = (1 - math.exp(-k * n / m)) ** k
print(f"false positive rate: measured {fp:.4f}, formula {theory:.4f} (10 bits per key, k = 7)")
