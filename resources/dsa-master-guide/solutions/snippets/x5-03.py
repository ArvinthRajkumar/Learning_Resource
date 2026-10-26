def sieve(n):
    is_p = [True] * (n + 1)
    is_p[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if is_p[i]:
            for j in range(i * i, n + 1, i): is_p[j] = False
    return [i for i, v in enumerate(is_p) if v]
def spf_sieve(n):
    spf = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j: spf[j] = i
    return spf
def fast_factor(x, spf):
    out = {}
    while x > 1:
        out[spf[x]] = out.get(spf[x], 0) + 1
        x //= spf[x]
    return out
def is_prime(n):
    if n < 2: return False
    return all(n % d for d in range(2, int(n ** 0.5) + 1))
P = sieve(1000)
assert P == [i for i in range(1001) if is_prime(i)]
spf = spf_sieve(1000)
print(len(P), "primes up to 1000; 840 =", fast_factor(840, spf), "; 997 =", fast_factor(997, spf))
