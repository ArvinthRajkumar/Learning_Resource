def min_coins_greedy(amount):
    count = 0
    for d in (2000, 500, 200, 100, 50, 20, 10, 5, 2, 1):
        q, amount = divmod(amount, d)
        count += q
    return count
