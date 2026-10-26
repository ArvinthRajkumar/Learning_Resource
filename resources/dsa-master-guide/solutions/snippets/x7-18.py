import itertools
def dutch(a):
    lo, mid, hi = 0, 0, len(a) - 1
    while mid <= hi:
        if a[mid] == 0: a[lo], a[mid] = a[mid], a[lo]; lo += 1; mid += 1
        elif a[mid] == 1: mid += 1
        else: a[mid], a[hi] = a[hi], a[mid]; hi -= 1
    return a
def next_perm(a):
    a = a[:]
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i + 1]: i -= 1
    if i >= 0:
        j = len(a) - 1
        while a[j] <= a[i]: j -= 1
        a[i], a[j] = a[j], a[i]
    a[i + 1:] = a[i + 1:][::-1]
    return a
assert dutch([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
perms = list(itertools.permutations([1, 2, 3, 4]))
assert all(tuple(next_perm(list(perms[i]))) == perms[i + 1] for i in range(len(perms) - 1))
print("verified; next of [3,2,1] wraps to", next_perm([3, 2, 1]))
