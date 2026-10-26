points_per_sec = 100_000 * 100 / 10
raw_tb_day = points_per_sec * 16 * 86_400 / 1e12
comp_tb_day = points_per_sec * 1.5 * 86_400 / 1e12
print(int(points_per_sec), "points/s;", round(raw_tb_day, 2), "TB/day raw;", round(comp_tb_day, 2), "TB/day compressed")
