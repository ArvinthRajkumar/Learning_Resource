def assign_cookies(g, s):
    g, s = sorted(g), sorted(s)
    child = 0
    for cookie in s:
        if child < len(g) and cookie >= g[child]:
            child += 1
    return child
