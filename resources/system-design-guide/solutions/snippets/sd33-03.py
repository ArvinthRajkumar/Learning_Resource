import heapq
shards = [[(0.9, "doc1"), (0.5, "doc4"), (0.1, "doc7")], [(0.8, "doc2"), (0.7, "doc5")], [(0.95, "doc3"), (0.2, "doc9")]]
def scatter_gather(shards, k):
    top_per_shard = [sorted(s, reverse=True)[:k] for s in shards]               # each shard answers locally
    return heapq.nlargest(k, (hit for hits in top_per_shard for hit in hits))   # coordinator merges
print("global top 3 from three shards:", scatter_gather(shards, 3))
