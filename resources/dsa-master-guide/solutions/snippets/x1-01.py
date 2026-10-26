import random
random.seed(0)
a = [random.randint(-9, 9) for _ in range(20)]
prefix = [0]
for x in a:
    prefix.append(prefix[-1] + x)
def range_sum(l, r): return prefix[r] - prefix[l]
assert all(range_sum(l, r) == sum(a[l:r]) for l in range(21) for r in range(l, 21))
print("prefix sums verified on all", 21 * 22 // 2, "ranges")
