import math, random
random.seed(2)
def mo_distinct(a, queries):
    n = len(a); B = max(1, int(n / math.sqrt(max(1, len(queries)))))
    order = sorted(range(len(queries)), key=lambda i: (queries[i][0] // B, queries[i][1] if (queries[i][0] // B) % 2 == 0 else -queries[i][1]))
    count, distinct, L, R, ans, moves = {}, 0, 0, -1, [0] * len(queries), 0
    def add(i):
        nonlocal distinct
        count[a[i]] = count.get(a[i], 0) + 1
        if count[a[i]] == 1: distinct += 1
    def remove(i):
        nonlocal distinct
        count[a[i]] -= 1
        if count[a[i]] == 0: distinct -= 1
    for qi in order:
        l, r = queries[qi]
        while L > l: L -= 1; add(L); moves += 1
        while R < r: R += 1; add(R); moves += 1
        while L < l: remove(L); L += 1; moves += 1
        while R > r: remove(R); R -= 1; moves += 1
        ans[qi] = distinct
    return ans, moves
n, q = 2000, 2000
a = [random.randint(0, 50) for _ in range(n)]
queries = []
for _ in range(q):
    l = random.randrange(n); queries.append((l, random.randrange(l, n)))
ans, moves = mo_distinct(a, queries)
for i in random.sample(range(q), 200): assert ans[i] == len(set(a[queries[i][0]:queries[i][1] + 1]))
naive_work = sum(r - l + 1 for l, r in queries)
print(f"Mo's answers verified | window moves {moves:,} versus {naive_work:,} element visits for the naive approach")
