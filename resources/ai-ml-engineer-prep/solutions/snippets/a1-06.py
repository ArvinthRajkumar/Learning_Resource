def gini(labels):
    n = len(labels)
    return 1 - sum((labels.count(c) / n) ** 2 for c in set(labels)) if n else 0
data = [(2.0, 0), (3.0, 0), (4.0, 0), (6.0, 1), (7.0, 1), (8.0, 1), (5.0, 0), (5.5, 1)]
data.sort()
best = None
for i in range(1, len(data)):
    thr = (data[i - 1][0] + data[i][0]) / 2
    left = [y for x, y in data if x <= thr]
    right = [y for x, y in data if x > thr]
    g = (len(left) * gini(left) + len(right) * gini(right)) / len(data)
    if best is None or g < best[0]:
        best = (g, thr)
print("best threshold %.2f with weighted gini %.3f (parent gini %.3f)" % (best[1], best[0], gini([y for _, y in data])))
