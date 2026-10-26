import random
random.seed(3)
def gossip_rounds(n, fanout=2):
    informed, rounds = {0}, 0
    while len(informed) < n:
        new = set()
        for node in informed:
            new |= set(random.sample(range(n), fanout))
        informed |= new; rounds += 1
    return rounds
for n in (10, 100, 1000, 10000):
    print(f"{n:>6} nodes: all informed after {gossip_rounds(n)} rounds")
