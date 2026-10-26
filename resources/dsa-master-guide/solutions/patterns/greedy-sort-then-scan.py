def max_activities(intervals):
    count, last_end = 0, float("-inf")
    for s, e in sorted(intervals, key=lambda x: x[1]):
        if s >= last_end:
            count += 1
            last_end = e
    return count
