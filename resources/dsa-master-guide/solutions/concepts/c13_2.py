import heapq

def kth_largest(nums, k):
    heap = []                          # min-heap holding the k largest
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)        # discard the smallest
    return heap[0]
