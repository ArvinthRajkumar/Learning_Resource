import itertools
def subsets(a):
    out = []
    def go(i, cur):
        if i == len(a): out.append(cur[:]); return
        go(i + 1, cur)
        cur.append(a[i]); go(i + 1, cur); cur.pop()
    go(0, []); return out
def combination_sum(c, t):
    out = []
    def go(i, rem, cur):
        if rem == 0: out.append(cur[:]); return
        for j in range(i, len(c)):
            if c[j] <= rem:
                cur.append(c[j]); go(j, rem - c[j], cur); cur.pop()
    go(0, t, []); return out
assert len(subsets([1, 2, 3, 4])) == 16
assert sorted(map(tuple, subsets([1, 2, 3]))) == sorted(sum((list(itertools.combinations([1, 2, 3], r)) for r in range(4)), []))
print(combination_sum([2, 3, 6, 7], 7), len(combination_sum([1, 2, 5], 11)))
