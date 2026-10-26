import heapq
a, b, c = [1, 4, 9], [2, 3, 10], [0, 5]
merged = heapq.merge(a, b, c)                 # an iterator: nothing is built yet
print(list(merged))
