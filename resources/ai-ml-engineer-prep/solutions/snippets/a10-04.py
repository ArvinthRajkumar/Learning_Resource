import math, random
random.seed(2)
# A 2-armed bandit with a softmax policy; REINFORCE with a running baseline.
arm_reward = [0.3, 0.7]
theta = [0.0, 0.0]
def pi(th):
    m = max(th); e = [math.exp(t - m) for t in th]; s = sum(e); return [x / s for x in e]
baseline = 0.0
for _ in range(3000):
    p = pi(theta)
    a = random.choices([0, 1], p)[0]
    r = 1.0 if random.random() < arm_reward[a] else 0.0
    adv = r - baseline
    baseline += 0.01 * (r - baseline)
    for i in range(2):
        theta[i] += 0.1 * adv * ((1 if i == a else 0) - p[i])
print("policy probabilities:", [round(x, 3) for x in pi(theta)])
