def greedy_coins(amount, coins):
    out = []
    for c in sorted(coins, reverse=True):
        while amount >= c: amount -= c; out.append(c)
    return out
print("coins 1,5,10,25 for 63:", greedy_coins(63, [1, 5, 10, 25]), "| greedy fails for coins 1,3,4 and amount 6:", greedy_coins(6, [1, 3, 4]), "uses 3 coins, but 3 + 3 uses only 2")
