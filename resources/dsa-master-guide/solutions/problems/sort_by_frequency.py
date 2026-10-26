from collections import Counter

def sort_by_frequency(nums):
    freq = Counter(nums)
    return sorted(nums, key=lambda x: (-freq[x], x))
