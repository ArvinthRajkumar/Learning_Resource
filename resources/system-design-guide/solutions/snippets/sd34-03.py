import random
random.seed(2)
def storm(clients, backoff, jitter):
    load = {}
    for _ in range(clients):
        t = backoff * (random.random() if jitter else 1)
        load[round(t, 1)] = load.get(round(t, 1), 0) + 1
    return max(load.values())
print("1000 clients all retry after 2 s:", storm(1000, 2, False), "requests land in the same instant")
print("with random jitter over 2 s:      ", storm(1000, 2, True), "requests in the busiest 0.1 s slot")
