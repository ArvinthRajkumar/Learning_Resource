from collections import Counter
def first_unique(s):
    c = Counter(s)
    return next((i for i, ch in enumerate(s) if c[ch] == 1), -1)
print(first_unique("leetcode"), first_unique("aabb"))
