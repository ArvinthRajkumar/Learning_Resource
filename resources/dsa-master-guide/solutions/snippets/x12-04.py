import heapq
data = [9, 4, 7, 1, 8, 2, 6]
print("3 smallest:", heapq.nsmallest(3, data))
heap = list(data)
heapq.heapify(heap)                                            # O(n): only the top is guaranteed to be the smallest
print("internal heap array (not sorted):", heap, "| top is the minimum:", heap[0])
print("popping repeatedly yields sorted order:", [heapq.heappop(heap) for _ in range(len(heap))])
