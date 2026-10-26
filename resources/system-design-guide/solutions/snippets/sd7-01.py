t_cache, t_db = 1, 20          # milliseconds
for hit in (0.0, 0.5, 0.9, 0.99):
    t = hit * t_cache + (1 - hit) * t_db
    print("hit rate %.2f -> average %.2f ms" % (hit, t))
