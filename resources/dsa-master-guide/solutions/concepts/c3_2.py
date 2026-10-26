def find_duplicates(nums):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1    # count occurrences
    return [k for k, v in freq.items() if v > 1]
