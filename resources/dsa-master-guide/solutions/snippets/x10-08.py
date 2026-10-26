import random, itertools
from functools import lru_cache
random.seed(4)
@lru_cache(None)
def nim_wins(piles):
    for i, p in enumerate(piles):
        for take in range(1, p + 1):
            nxt = tuple(sorted(piles[:i] + (p - take,) + piles[i + 1:]))
            if not nim_wins(nxt): return True
    return False
def nim_by_xor(piles):
    x = 0
    for p in piles: x ^= p
    return x != 0
for _ in range(100):
    piles = tuple(sorted(random.randint(0, 5) for _ in range(random.randint(1, 4))))
    assert nim_wins(piles) == nim_by_xor(piles), piles
print("Bouton's theorem verified against exhaustive game search on 100 random Nim positions")
def winning_move(piles):
    x = 0
    for p in piles: x ^= p
    for i, p in enumerate(piles):
        if p ^ x < p: return i, p - (p ^ x)                 # reduce pile i by this many stones
print("from piles (3, 4, 5) the winning move is (pile index, stones to take):", winning_move((3, 4, 5)))
