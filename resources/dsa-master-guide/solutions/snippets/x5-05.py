MOD = 10**9 + 7
inv = lambda a: pow(a, MOD - 2, MOD)
for a in [2, 3, 12345, 10**9]:
    assert a * inv(a) % MOD == 1 and pow(a, -1, MOD) == inv(a)
print("inverse of 2 mod 1e9+7:", inv(2), "| 7/3 mod p =", 7 * inv(3) % MOD)
