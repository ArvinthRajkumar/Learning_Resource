def counter_flips(n):
    bits, flips = [0] * 40, 0
    for _ in range(n):
        i = 0
        while bits[i] == 1:
            bits[i] = 0; flips += 1; i += 1
        bits[i] = 1; flips += 1
    return flips
for n in [100, 1000, 10**5]:
    print(n, "increments ->", counter_flips(n), "flips (ratio", round(counter_flips(n) / n, 3), ")")
