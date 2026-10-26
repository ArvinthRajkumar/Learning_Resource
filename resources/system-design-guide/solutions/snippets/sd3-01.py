import random
random.seed(1)
servers = 3
# each request has a "cost" in time units; a few are very expensive
reqs = [1] * 40 + [20] * 4
random.shuffle(reqs)

# round robin: assign in order
load_rr = [0] * servers
for i, c in enumerate(reqs):
    load_rr[i % servers] += c

# least loaded (a proxy for least connections / least work)
load_lc = [0] * servers
for c in reqs:
    j = min(range(servers), key=lambda k: load_lc[k])
    load_lc[j] += c

print("round robin  :", load_rr, "max", max(load_rr))
print("least loaded :", load_lc, "max", max(load_lc))
