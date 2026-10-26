def is_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
def factorize(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
print([p for p in range(30) if is_prime(p)])
print(factorize(360), factorize(97), factorize(1001))
