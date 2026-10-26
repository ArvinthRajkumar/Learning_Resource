def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a // gcd(a, b) * b

def sieve(n):                             # primes <= n
    is_p = [True] * (n + 1)
    is_p[0:2] = [False, False]
    for p in range(2, int(n ** 0.5) + 1):
        if is_p[p]:
            for m in range(p * p, n + 1, p):
                is_p[m] = False
    return [i for i, ok in enumerate(is_p) if ok]

def prime_factors(n):
    res, d = [], 2
    while d * d <= n:
        while n % d == 0:
            res.append(d)
            n //= d
        d += 1
    if n > 1:
        res.append(n)
    return res
