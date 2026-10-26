import random
random.seed(2)
def longest_consecutive(a):
    s, best = set(a), 0
    for x in s:
        if x - 1 not in s:
            y = x
            while y + 1 in s: y += 1
            best = max(best, y - x + 1)
    return best
def brute(a):
    s, best = set(a), 0
    for x in s:
        y = x
        while y in s: y += 1
        best = max(best, y - x)
    return best
for _ in range(300):
    a = [random.randint(0, 15) for _ in range(random.randint(0, 12))]
    assert longest_consecutive(a) == brute(a)
print("verified;", longest_consecutive([100, 4, 200, 1, 3, 2]))
