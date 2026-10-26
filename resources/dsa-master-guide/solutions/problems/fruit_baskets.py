from collections import defaultdict

def fruit_baskets(fruits):
    count = defaultdict(int)
    left = best = 0
    for right, f in enumerate(fruits):
        count[f] += 1
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1
        best = max(best, right - left + 1)
    return best
