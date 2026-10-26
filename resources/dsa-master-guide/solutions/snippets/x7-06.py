import heapq, random
from collections import Counter
random.seed(5)
def top_k(a, k):
    cnt = Counter(a)
    return sorted(heapq.nlargest(k, cnt, key=lambda x: (cnt[x], -x)))
def brute(a, k):
    cnt = Counter(a)
    return sorted(sorted(cnt, key=lambda x: (-cnt[x], x))[:k])
for _ in range(300):
    a = [random.randint(0, 5) for _ in range(random.randint(1, 15))]
    k = random.randint(1, len(set(a)))
    assert top_k(a, k) == brute(a, k)
print("verified;", top_k([1, 1, 1, 2, 2, 3], 2))
