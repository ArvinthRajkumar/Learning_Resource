def rrf(rankings, k=60):
    scores = {}
    for ranking in rankings:
        for pos, doc in enumerate(ranking, 1):
            scores[doc] = scores.get(doc, 0) + 1 / (k + pos)
    return sorted(scores, key=lambda d: -scores[d])
dense = ["d3", "d1", "d7", "d2"]
bm25 = ["d7", "d3", "d9", "d1"]
print(rrf([dense, bm25]))
