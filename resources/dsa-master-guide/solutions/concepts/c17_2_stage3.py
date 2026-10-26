def count_primes(n):
    if n < 3:
        return 0
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            for m in range(p * p, n, p):
                sieve[m] = False
    return sum(sieve)
