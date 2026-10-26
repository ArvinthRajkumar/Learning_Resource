import math
def dcg(rels, k): return sum((2 ** r - 1) / math.log2(i + 2) for i, r in enumerate(rels[:k]))
def ndcg(rels, k):
    ideal = sorted(rels, reverse=True)
    return dcg(rels, k) / dcg(ideal, k)
print("relevant item first : %.3f" % ndcg([3, 2, 0, 0], 4))
print("relevant item last  : %.3f" % ndcg([0, 0, 2, 3], 4))
rank_of_first_hit = [1, 3, 2]
print("MRR = %.3f" % (sum(1 / r for r in rank_of_first_hit) / len(rank_of_first_hit)))
