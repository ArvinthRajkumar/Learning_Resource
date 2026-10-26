import heapq

def running_median(nums):
    low, high, out = [], [], []     # low: max-heap (negated), high: min-heap
    for x in nums:
        heapq.heappush(low, -x)
        heapq.heappush(high, -heapq.heappop(low))   # keep halves ordered
        if len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))
        if len(low) > len(high):
            out.append(-low[0])
        else:
            out.append((-low[0] + high[0]) / 2)
    return out
