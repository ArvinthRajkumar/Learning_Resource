def power(a, b, m):
    result, a = 1, a % m
    while b:
        if b & 1: result = result * a % m
        a = a * a % m
        b >>= 1
    return result
assert all(power(a, b, 1000003) == pow(a, b, 1000003) for a in range(1, 40) for b in range(0, 60))
print(power(2, 10, 1000), power(3, 200, 10**9 + 7), pow(3, 200, 10**9 + 7))
