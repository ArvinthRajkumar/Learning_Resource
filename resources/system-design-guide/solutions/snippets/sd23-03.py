import math
def dcg(rels): return sum(r / math.log2(i + 2) for i, r in enumerate(rels))
def ndcg(rels):
    ideal = dcg(sorted(rels, reverse=True))
    return dcg(rels) / ideal if ideal else 0.0
print("relevant item first :", round(ndcg([3, 2, 0, 0]), 3))
print("relevant item last  :", round(ndcg([0, 0, 2, 3]), 3))
