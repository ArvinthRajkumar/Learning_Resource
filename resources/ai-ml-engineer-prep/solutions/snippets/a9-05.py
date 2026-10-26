import random
random.seed(1)
true_ctr = [0.04, 0.05, 0.08]            # click rates of 3 items, unknown to the algorithm
def run(strategy, steps=20000):
    wins, plays, reward = [0, 0, 0], [0, 0, 0], 0
    for _ in range(steps):
        if strategy == "random":
            a = random.randrange(3)
        elif strategy == "thompson":
            a = max(range(3), key=lambda i: random.betavariate(1 + wins[i], 1 + plays[i] - wins[i]))
        else:                            # epsilon greedy
            a = random.randrange(3) if random.random() < 0.1 or 0 in plays else max(range(3), key=lambda i: wins[i] / plays[i])
        click = random.random() < true_ctr[a]
        plays[a] += 1; wins[a] += click; reward += click
    return reward, plays
for s in ("random", "epsilon", "thompson"):
    r, p = run(s)
    print("%-9s total clicks %4d, plays per item %s" % (s, r, p))
