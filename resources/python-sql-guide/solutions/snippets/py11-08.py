import cProfile, pstats, io
def slow_unique(items):
    out = []
    for x in items:
        if x not in out: out.append(x)               # O(n) membership in a list -> O(n^2) overall
    return out
def fast_unique(items):
    seen, out = set(), []
    for x in items:
        if x not in seen: seen.add(x); out.append(x)
    return out
data = [i % 2000 for i in range(20000)]
pr = cProfile.Profile(); pr.enable(); slow_unique(data); pr.disable()
stats = pstats.Stats(pr, stream=io.StringIO()).sort_stats("tottime")
slow_calls = {fn[2]: v[1] for fn, v in stats.stats.items()}
print("cProfile recorded one call to slow_unique:", slow_calls.get("slow_unique"))
import timeit
t_slow = timeit.timeit(lambda: slow_unique(data), number=1)
t_fast = timeit.timeit(lambda: fast_unique(data), number=1)
print("same result:", slow_unique(data) == fast_unique(data), "| the set-based version is at least 10x faster:", t_slow / t_fast > 10)
