import math
n = 1_000_000
print("worst-case guesses for 1,000,000 sorted items:", math.ceil(math.log2(n)), "versus up to", n, "for a linear scan")
