def coins(c, amount):
    n = 0
    for x in sorted(c, reverse=True):
        n += amount // x
        amount %= x
    return n if amount == 0 else -1
