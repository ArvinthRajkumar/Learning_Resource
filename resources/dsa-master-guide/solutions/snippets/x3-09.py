from functools import lru_cache
def count_no_digit_7(N):
    digits = list(map(int, str(N)))
    @lru_cache(None)
    def go(pos, tight):
        if pos == len(digits): return 1
        total = 0
        for d in range(0, (digits[pos] if tight else 9) + 1):
            if d == 7: continue
            total += go(pos + 1, tight and d == digits[pos])
        return total
    return go(0, True)
brute = lambda N: sum(1 for x in range(N + 1) if "7" not in str(x))
assert all(count_no_digit_7(N) == brute(N) for N in (0, 6, 7, 70, 99, 100, 777, 1234))
print("digit DP verified; count up to 10^18:", count_no_digit_7(10 ** 18))
