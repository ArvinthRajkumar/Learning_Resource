def min_platforms(arr, dep):
    arr, dep = sorted(arr), sorted(dep)
    i = j = 0
    cur = best = 0
    while i < len(arr):
        if arr[i] <= dep[j]:       # next event is an arrival
            cur += 1
            i += 1
            best = max(best, cur)
        else:                      # a train leaves
            cur -= 1
            j += 1
    return best
