def longest_at_most_k_distinct(s, k):
    cnt, left, best = {}, 0, 0
    for right, ch in enumerate(s):
        cnt[ch] = cnt.get(ch, 0) + 1
        while len(cnt) > k:
            cnt[s[left]] -= 1
            if cnt[s[left]] == 0:
                del cnt[s[left]]
            left += 1
        best = max(best, right - left + 1)
    return best
