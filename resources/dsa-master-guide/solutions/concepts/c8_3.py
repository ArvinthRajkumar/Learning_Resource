def longest_without_repeat(s):
    last = {}                       # char -> last index
    left = best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1     # jump past the duplicate
        last[ch] = right
        best = max(best, right - left + 1)
    return best
