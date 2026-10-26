import bisect, random
random.seed(2)
def lis_fast(a):
    tails = []
    for x in a:
        i = bisect.bisect_left(tails, x)
        if i == len(tails): tails.append(x)
        else: tails[i] = x
    return len(tails)
def lis_slow(a):
    dp = [1] * len(a)
    for i in range(len(a)):
        for j in range(i):
            if a[j] < a[i]: dp[i] = max(dp[i], dp[j] + 1)
    return max(dp, default=0)
for _ in range(200):
    a = [random.randint(0, 20) for _ in range(random.randint(0, 15))]
    assert lis_fast(a) == lis_slow(a)
print("O(n log n) LIS matches the O(n^2) DP; example:", lis_fast([10, 9, 2, 5, 3, 7, 101, 18]))
