import heapq

def kth_largest(nums, k):
    heap = []                        # min-heap with the k largest values
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)      # drop the smallest
    return heap[0]
