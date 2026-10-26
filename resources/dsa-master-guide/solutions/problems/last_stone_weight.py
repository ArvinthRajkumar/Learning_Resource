import heapq

def last_stone_weight(stones):
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        a = -heapq.heappop(heap)       # heaviest
        b = -heapq.heappop(heap)       # second heaviest
        if a != b:
            heapq.heappush(heap, -(a - b))
    return -heap[0] if heap else 0
