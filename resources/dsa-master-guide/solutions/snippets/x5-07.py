import math, itertools
MOD = 10**9 + 7
N = 2000
fact = [1] * (N + 1)
for i in range(1, N + 1): fact[i] = fact[i - 1] * i % MOD
ifact = [pow(f, MOD - 2, MOD) for f in fact]
def ncr(n, r):
    return 0 if r < 0 or r > n else fact[n] * ifact[r] % MOD * ifact[n - r] % MOD
assert all(ncr(n, r) == math.comb(n, r) % MOD for n in range(0, 60) for r in range(0, n + 1))
# derangements by recurrence vs brute force
D = [1, 0]
for n in range(2, 8): D.append((n - 1) * (D[-1] + D[-2]))
brute = lambda n: sum(all(p[i] != i for i in range(n)) for p in itertools.permutations(range(n)))
assert all(D[n] == brute(n) for n in range(0, 8))
catalan = lambda n: math.comb(2 * n, n) // (n + 1)
print("nCr table verified; C(1000,500) mod p =", ncr(1000, 500), "| derangements:", D, "| Catalan:", [catalan(n) for n in range(8)])
