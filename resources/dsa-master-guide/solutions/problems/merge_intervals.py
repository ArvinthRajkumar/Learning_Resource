def merge_intervals(intervals):
    res = []
    for start, end in sorted(intervals):
        if res and start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)    # overlap -> extend
        else:
            res.append([start, end])
    return res
