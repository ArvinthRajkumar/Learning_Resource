import random, itertools
random.seed(3)
def matrix_chain(dims):                          # dims of matrices: A_i is dims[i-1] x dims[i]
    n = len(dims) - 1
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            dp[l][r] = min(dp[l][k] + dp[k + 1][r] + dims[l] * dims[k + 1] * dims[r + 1] for k in range(l, r))
    return dp[0][n - 1]
def brute(dims):
    def go(l, r):
        if l == r: return 0
        return min(go(l, k) + go(k + 1, r) + dims[l] * dims[k + 1] * dims[r + 1] for k in range(l, r))
    return go(0, len(dims) - 2)
for _ in range(30):
    dims = [random.randint(1, 9) for _ in range(random.randint(2, 7))]
    assert matrix_chain(dims) == brute(dims)
print("matrix chain verified; classic example [40, 20, 30, 10, 30] ->", matrix_chain([40, 20, 30, 10, 30]))

def burst_balloons(nums):
    a = [1] + nums + [1]; n = len(a)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for l in range(n - length):
            r = l + length
            dp[l][r] = max(dp[l][k] + a[l] * a[k] * a[r] + dp[k][r] for k in range(l + 1, r))
    return dp[0][n - 1]
print("burst balloons [3, 1, 5, 8] ->", burst_balloons([3, 1, 5, 8]))
