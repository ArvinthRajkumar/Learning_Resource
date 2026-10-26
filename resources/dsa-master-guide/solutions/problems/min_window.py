from collections import Counter

def min_window(s, t):
    need = Counter(t)
    missing = len(need)
    left = 0
    best = (float("inf"), 0, 0)
    for right, ch in enumerate(s):
        if ch in need:
            need[ch] -= 1
            if need[ch] == 0:
                missing -= 1
        while missing == 0:                      # window is valid: shrink
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right)
            out = s[left]
            if out in need:
                need[out] += 1
                if need[out] > 0:
                    missing += 1
            left += 1
    return "" if best[0] == float("inf") else s[best[1]:best[2] + 1]
