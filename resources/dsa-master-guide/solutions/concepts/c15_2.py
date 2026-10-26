def select_activities(starts, ends):
    chosen, last_end = [], float("-inf")
    for s, e in sorted(zip(starts, ends), key=lambda p: p[1]):
        if s >= last_end:                 # compatible with the last chosen
            chosen.append((s, e))
            last_end = e
    return chosen
