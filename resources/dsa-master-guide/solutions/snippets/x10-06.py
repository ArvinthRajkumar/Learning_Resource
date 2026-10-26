import heapq
def skyline(buildings):
    events = sorted([(l, -h, r) for l, r, h in buildings] + [(r, 0, 0) for l, r, h in buildings])
    result, heap = [], [(0, float("inf"))]                                     # (negative height, end)
    for x, negh, r in events:
        while heap[0][1] <= x: heapq.heappop(heap)                           # drop buildings that have ended
        if negh: heapq.heappush(heap, (negh, r))
        top = -heap[0][0]
        if not result or result[-1][1] != top: result.append([x, top])
    return result
print(skyline([(2, 9, 10), (3, 7, 15), (5, 12, 12), (15, 20, 10), (19, 24, 8)]))
