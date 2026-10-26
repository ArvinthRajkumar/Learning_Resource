import time
from concurrent.futures import ThreadPoolExecutor

def fetch(n):
    time.sleep(0.2)               # pretend this is a network call
    return n * n

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(fetch, range(5)))
elapsed = time.perf_counter() - start
print(results, "fast:", elapsed < 0.6)          # five 0.2s waits overlap, about 0.2s total
