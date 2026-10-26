import random
from collections import defaultdict
random.seed(0)
def subarray_sum(a, k):
    seen, cur, ans = defaultdict(int), 0, 0
    seen[0] = 1
    for x in a:
        cur += x
        ans += seen[cur - k]
        seen[cur] += 1
    return ans
brute = lambda a, k: sum(sum(a[i:j]) == k for i in range(len(a)) for j in range(i + 1, len(a) + 1))
for _ in range(300):
    a = [random.randint(-3, 3) for _ in range(random.randint(0, 10))]
    k = random.randint(-4, 4)
    assert subarray_sum(a, k) == brute(a, k)
print("subarray sum = k verified; example:", subarray_sum([1, 2, 3, -3, 3], 3))
