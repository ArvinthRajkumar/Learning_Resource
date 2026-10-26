import random
random.seed(11)
def reconnect_peak(clients, jitter_window):
    buckets = {}
    for _ in range(clients):
        t = int(random.uniform(0, jitter_window))          # each client picks a random delay
        buckets[t] = buckets.get(t, 0) + 1
    return max(buckets.values())
for window in (1, 10, 60):
    print(f"1,000,000 clients reconnecting spread over {window:>2} s: busiest second sees {reconnect_peak(1_000_000, window):>9,} connections")
