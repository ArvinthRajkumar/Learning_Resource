def count_primes(n):
    def is_p(x):
        if x < 2:
            return False
        d = 2
        while d * d <= x:
            if x % d == 0:
                return False
            d += 1
        return True
    return sum(is_p(x) for x in range(n))
