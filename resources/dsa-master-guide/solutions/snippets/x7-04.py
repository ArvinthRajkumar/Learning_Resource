import random
from collections import Counter
random.seed(3)
def majority(a):
    cand, cnt = None, 0
    for x in a:
        if cnt == 0: cand = x
        cnt += 1 if x == cand else -1
    return cand if a.count(cand) > len(a) // 2 else None
for _ in range(300):
    a = [random.randint(0, 2) for _ in range(random.randint(1, 11))]
    c, f = Counter(a).most_common(1)[0]
    assert majority(a) == (c if f > len(a) // 2 else None)
print("verified;", majority([2, 2, 1, 1, 2, 2, 3]))
