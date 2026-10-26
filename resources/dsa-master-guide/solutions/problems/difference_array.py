def difference_array(n, updates):
    diff = [0] * (n + 1)
    for l, r, v in updates:
        diff[l] += v
        diff[r + 1] -= v
    res, running = [], 0
    for i in range(n):
        running += diff[i]
        res.append(running)
    return res
