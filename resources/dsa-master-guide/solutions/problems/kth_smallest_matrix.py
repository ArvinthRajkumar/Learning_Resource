import heapq

def kth_smallest_matrix(matrix, k):
    heap = [(row[0], r, 0) for r, row in enumerate(matrix)]
    heapq.heapify(heap)
    for _ in range(k):
        val, r, c = heapq.heappop(heap)
        if c + 1 < len(matrix[r]):
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
    return val
