a = 0.999
series = a * a * a
parallel_two = 1 - (1 - a) ** 2
print("3 in series:", round(series * 100, 4))
print("2 in parallel:", round(parallel_two * 100, 6))
