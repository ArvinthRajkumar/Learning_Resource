from collections import defaultdict

def longest_repeating_replace(s, k):
    count = defaultdict(int)
    left = best = most = 0
    for right, ch in enumerate(s):
        count[ch] += 1
        most = max(most, count[ch])
        while (right - left + 1) - most > k:
            count[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
