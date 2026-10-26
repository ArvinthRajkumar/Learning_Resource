def overlap(n, w, r):
    return r + w > n
for n, w, r in [(3, 2, 2), (3, 3, 1), (3, 1, 3), (3, 1, 1), (5, 3, 3)]:
    print("N=%d W=%d R=%d  strongly overlapping: %s" % (n, w, r, overlap(n, w, r)))
