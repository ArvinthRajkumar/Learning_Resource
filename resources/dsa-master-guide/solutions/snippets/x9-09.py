import random
random.seed(9)
def at_most_k_distinct(a, k):
    count, left, total = {}, 0, 0
    for right, x in enumerate(a):
        count[x] = count.get(x, 0) + 1
        while len(count) > k:
            count[a[left]] -= 1
            if count[a[left]] == 0: del count[a[left]]
            left += 1
        total += right - left + 1                                     # all subarrays ending at right
    return total
def exactly_k_distinct(a, k): return at_most_k_distinct(a, k) - at_most_k_distinct(a, k - 1)
for _ in range(300):
    a = [random.randint(1, 4) for _ in range(random.randint(0, 12))]; k = random.randint(1, 3)
    brute = sum(1 for i in range(len(a)) for j in range(i + 1, len(a) + 1) if len(set(a[i:j])) == k)
    assert exactly_k_distinct(a, k) == brute
print("subarrays with exactly k distinct values verified | [1,2,1,2,3] with k=2:", exactly_k_distinct([1, 2, 1, 2, 3], 2))
