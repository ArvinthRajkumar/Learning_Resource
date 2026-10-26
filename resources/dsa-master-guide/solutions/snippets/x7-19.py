import random
random.seed(14)
def largest_rect(h):
    stack, best = [], 0
    for i, x in enumerate(h + [0]):
        start = i
        while stack and stack[-1][1] >= x:
            idx, height = stack.pop()
            best = max(best, height * (i - idx)); start = idx
        stack.append((start, x))
    return best
brute = lambda h: max((min(h[i:j + 1]) * (j - i + 1) for i in range(len(h)) for j in range(i, len(h))), default=0)
for _ in range(300):
    h = [random.randint(0, 6) for _ in range(random.randint(1, 10))]
    assert largest_rect(h) == brute(h)
print("verified;", largest_rect([2, 1, 5, 6, 2, 3]))
