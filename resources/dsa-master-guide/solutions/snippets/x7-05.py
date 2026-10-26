import random
random.seed(4)
def trap(h):
    l, r, lm, rm, water = 0, len(h) - 1, 0, 0, 0
    while l < r:
        if h[l] < h[r]:
            lm = max(lm, h[l]); water += lm - h[l]; l += 1
        else:
            rm = max(rm, h[r]); water += rm - h[r]; r -= 1
    return water
brute = lambda h: sum(max(0, min(max(h[:i + 1]), max(h[i:])) - h[i]) for i in range(len(h)))
for _ in range(300):
    h = [random.randint(0, 6) for _ in range(random.randint(1, 12))]
    assert trap(h) == brute(h)
print("verified;", trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
