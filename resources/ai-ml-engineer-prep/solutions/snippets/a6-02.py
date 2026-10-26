import math, random
random.seed(0)
# REINFORCE on a 3-armed bandit with a baseline: the policy learns to prefer the arm with highest reward.
rewards = [0.2, 0.8, 0.5]
logits = [0.0, 0.0, 0.0]
def probs(l):
    m = max(l); e = [math.exp(x - m) for x in l]; s = sum(e); return [x / s for x in e]
baseline, lr = 0.0, 0.1
for step in range(2000):
    p = probs(logits)
    a = random.choices(range(3), weights=p)[0]
    r = rewards[a] + random.gauss(0, 0.1)
    adv = r - baseline
    baseline += 0.05 * (r - baseline)
    for i in range(3):
        logits[i] += lr * adv * ((1 if i == a else 0) - p[i])        # grad of log pi(a)
print([round(x, 2) for x in probs(logits)])
