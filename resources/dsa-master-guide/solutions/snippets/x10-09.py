import random
from functools import lru_cache
random.seed(5)
MOVES = (1, 3, 4)                                            # subtraction game: remove 1, 3 or 4 stones from a pile
@lru_cache(None)
def grundy(n):
    reach = {grundy(n - m) for m in MOVES if m <= n}
    g = 0
    while g in reach: g += 1                                 # mex
    return g
print("Grundy numbers of pile sizes 0..15:", [grundy(n) for n in range(16)])
@lru_cache(None)
def sum_wins(piles):                                         # exhaustive search of the sum of subtraction games
    for i, p in enumerate(piles):
        for m in MOVES:
            if m <= p and not sum_wins(tuple(sorted(piles[:i] + (p - m,) + piles[i + 1:]))): return True
    return False
for _ in range(100):
    piles = tuple(sorted(random.randint(0, 9) for _ in range(random.randint(1, 3))))
    x = 0
    for p in piles: x ^= grundy(p)
    assert sum_wins(piles) == (x != 0), piles
print("XOR of Grundy numbers predicts the winner of sums of subtraction games on 100 random positions")
