def non_overlapping_intervals(intervals):
    removed, last_end = 0, float("-inf")
    for start, end in sorted(intervals, key=lambda x: x[1]):
        if start >= last_end:
            last_end = end
        else:
            removed += 1
    return removed
