import math
from functools import lru_cache
@lru_cache(None)
def T(n):  # merge sort comparisons-like recurrence
    return 0 if n <= 1 else T(n // 2) + T(n - n // 2) + n
@lru_cache(None)
def K(n):  # Karatsuba-like: 3 subproblems of half size plus linear work
    return 1 if n <= 1 else 3 * K(n // 2) + n
for n in [2**10, 2**14, 2**18]:
    print(f"n = 2^{int(math.log2(n)):>2}: T/(n log n) = {T(n) / (n * math.log2(n)):.3f} | K/n^1.585 = {K(n) / n ** math.log2(3):.3f}")
