import heapq, random
random.seed(6)
def merge(iv):
    out = []
    for s, e in sorted(iv):
        if out and s <= out[-1][1]: out[-1][1] = max(out[-1][1], e)
        else: out.append([s, e])
    return out
def min_rooms(iv):
    heap, best = [], 0
    for s, e in sorted(iv):
        while heap and heap[0] <= s: heapq.heappop(heap)
        heapq.heappush(heap, e)
        best = max(best, len(heap))
    return best
def rooms_brute(iv):
    return max((sum(s <= t < e for s, e in iv) for t in range(0, 20)), default=0)
for _ in range(300):
    iv = []
    for _ in range(random.randint(1, 8)):
        s = random.randint(0, 15); iv.append((s, s + random.randint(1, 4)))
    assert min_rooms(iv) == rooms_brute(iv)
print("rooms verified;", merge([(1, 3), (2, 6), (8, 10), (15, 18)]), min_rooms([(0, 30), (5, 10), (15, 20)]))
