MOD = 1_000_000_007

def ncr_mod(n, r):
    if r < 0 or r > n:
        return 0
    num = den = 1
    for i in range(r):
        num = num * (n - i) % MOD
        den = den * (i + 1) % MOD
    return num * pow(den, MOD - 2, MOD) % MOD
