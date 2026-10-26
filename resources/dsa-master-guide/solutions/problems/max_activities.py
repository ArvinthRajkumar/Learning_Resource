def max_activities(starts, ends):
    count, last_end = 0, float("-inf")
    for s, e in sorted(zip(starts, ends), key=lambda p: p[1]):
        if s >= last_end:
            count += 1
            last_end = e
    return count
