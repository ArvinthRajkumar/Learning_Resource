import random
random.seed(13)
def quickselect(a, k):  # k-th smallest, 0-indexed
    a = a[:]
    lo, hi = 0, len(a) - 1
    while True:
        p = a[random.randint(lo, hi)]
        lt = [x for x in a[lo:hi + 1] if x < p]
        eq = [x for x in a[lo:hi + 1] if x == p]
        gt = [x for x in a[lo:hi + 1] if x > p]
        if k - lo < len(lt): hi = lo + len(lt) - 1; a[lo:hi + 1] = lt
        elif k - lo < len(lt) + len(eq): return p
        else:
            new_lo = lo + len(lt) + len(eq)
            a[lo:hi + 1] = lt + eq + gt
            lo = new_lo
for _ in range(300):
    a = [random.randint(0, 20) for _ in range(random.randint(1, 15))]
    k = random.randrange(len(a))
    assert quickselect(a, k) == sorted(a)[k]
print("quickselect verified")
