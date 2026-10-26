import random, itertools
random.seed(3)
def count_inversions(a):
    if len(a) <= 1: return a, 0
    mid = len(a) // 2
    left, x = count_inversions(a[:mid]); right, y = count_inversions(a[mid:])
    merged, i, j, cross = [], 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: merged.append(left[i]); i += 1
        else: merged.append(right[j]); j += 1; cross += len(left) - i          # right[j] precedes all remaining left elements
    merged += left[i:] + right[j:]
    return merged, x + y + cross
for _ in range(300):
    a = [random.randint(0, 9) for _ in range(random.randint(0, 12))]
    assert count_inversions(a)[1] == sum(1 for i, j in itertools.combinations(range(len(a)), 2) if a[i] > a[j])
print("inversion counting verified | reversed list of 6 has", count_inversions([6, 5, 4, 3, 2, 1])[1], "inversions (15 = 6 choose 2)")
