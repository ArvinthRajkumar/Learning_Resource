import heapq
from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    return heapq.nsmallest(k, freq, key=lambda x: (-freq[x], x))
