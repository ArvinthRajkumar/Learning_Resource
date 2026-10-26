def count_primes(n):
    def is_p(x):
        return x > 1 and all(x % d for d in range(2, x))
    return sum(is_p(x) for x in range(n))
