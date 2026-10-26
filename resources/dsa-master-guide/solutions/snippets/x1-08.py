from collections import deque
import random
random.seed(6)
def sliding_max(a, k):
    dq, out = deque(), []                      # dq holds indices with decreasing values
    for i, x in enumerate(a):
        while dq and a[dq[-1]] <= x: dq.pop()
        dq.append(i)
        if dq[0] <= i - k: dq.popleft()
        if i >= k - 1: out.append(a[dq[0]])
    return out
a = [random.randint(0, 50) for _ in range(30)]
assert sliding_max(a, 5) == [max(a[i:i + 5]) for i in range(len(a) - 4)]
print("sliding window maximum verified; example:", sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
