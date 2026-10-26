import math
train = [((1, 1), "a"), ((1, 2), "a"), ((2, 1), "a"), ((6, 6), "b"), ((7, 6), "b"), ((6, 7), "b")]
def knn(q, k):
    nearest = sorted(train, key=lambda p: math.dist(p[0], q))[:k]
    votes = {}
    for _, label in nearest:
        votes[label] = votes.get(label, 0) + 1
    return max(votes, key=votes.get)
print(knn((2, 2), 3), knn((5, 5), 3), knn((4, 4), 1))
