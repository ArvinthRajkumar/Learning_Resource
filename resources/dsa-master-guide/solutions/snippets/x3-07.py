import itertools, random
random.seed(4)
def tsp(dist):
    n = len(dist)
    INF = float("inf")
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0                                      # start at city 0
    for mask in range(1 << n):
        for last in range(n):
            if dp[mask][last] == INF or not (mask >> last & 1): continue
            for nxt in range(n):
                if not (mask >> nxt & 1):
                    nm = mask | (1 << nxt)
                    dp[nm][nxt] = min(dp[nm][nxt], dp[mask][last] + dist[last][nxt])
    full = (1 << n) - 1
    return min(dp[full][last] + dist[last][0] for last in range(1, n))
def tsp_brute(dist):
    n = len(dist)
    return min(sum(dist[a][b] for a, b in zip((0,) + p, p + (0,))) for p in itertools.permutations(range(1, n)))
for _ in range(20):
    n = random.randint(3, 7)
    d = [[0 if i == j else random.randint(1, 20) for j in range(n)] for i in range(n)]
    assert tsp(d) == tsp_brute(d)
print("Held-Karp matches brute force over all permutations: O(2^n n^2) vs O(n!)")
