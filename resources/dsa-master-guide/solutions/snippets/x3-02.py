import itertools, random
random.seed(1)
def knapsack(items, W):
    dp = [0] * (W + 1)
    for w, v in items:
        for c in range(W, w - 1, -1):               # downwards: each item used at most once
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[W]
def brute(items, W):
    best = 0
    for mask in range(1 << len(items)):
        w = sum(items[i][0] for i in range(len(items)) if mask >> i & 1)
        if w <= W: best = max(best, sum(items[i][1] for i in range(len(items)) if mask >> i & 1))
    return best
for _ in range(80):
    items = [(random.randint(1, 8), random.randint(1, 20)) for _ in range(random.randint(1, 9))]
    W = random.randint(0, 20)
    assert knapsack(items, W) == brute(items, W)
print("0/1 knapsack verified against 2^n enumeration")
