import random
random.seed(2)
true_rates = [0.04, 0.05, 0.065]
def run(strategy, rounds=6000):
    wins, losses, reward = [1, 1, 1], [1, 1, 1], 0
    pulls = [0, 0, 0]
    for t in range(rounds):
        if strategy == "thompson": arm = max(range(3), key=lambda i: random.betavariate(wins[i], losses[i]))
        elif strategy == "uniform": arm = t % 3
        else: arm = max(range(3), key=lambda i: wins[i] / (wins[i] + losses[i])) if t > 30 else t % 3         # greedy after a short trial
        win = random.random() < true_rates[arm]
        wins[arm] += win; losses[arm] += 1 - win; reward += win; pulls[arm] += 1
    return reward, pulls
for s in ("uniform", "greedy", "thompson"):
    r, p = run(s); print(f"{s:>8}: conversions {r:4d} | pulls per arm {p}")
