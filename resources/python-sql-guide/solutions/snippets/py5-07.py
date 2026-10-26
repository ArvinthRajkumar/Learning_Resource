import cProfile, pstats, io

def slow():
    total = 0
    for i in range(200000):
        total += i % 7
    return total

pr = cProfile.Profile()
pr.enable(); slow(); pr.disable()
out = io.StringIO()
pstats.Stats(pr, stream=out).sort_stats("cumulative").print_stats(3)
print("profile captured:", "slow" in out.getvalue())
