# A 1D corridor of 5 states. Actions: left or right. Reaching the right end (state 4) gives reward 1 and ends.
N, gamma = 5, 0.9
V = [0.0] * N
def step(s, a):                          # deterministic transitions; a = -1 or +1
    s2 = min(max(s + a, 0), N - 1)
    return s2, (1.0 if s2 == N - 1 and s != N - 1 else 0.0)
for it in range(50):
    new = V[:]
    for s in range(N - 1):               # state N-1 is terminal with value 0
        best = -1e9
        for a in (-1, 1):
            s2, r = step(s, a)
            best = max(best, r + gamma * (0.0 if s2 == N - 1 else V[s2]))
        new[s] = best
    V = new
print("values:", [round(v, 3) for v in V])
policy = []
for s in range(N - 1):
    qs = {a: step(s, a)[1] + gamma * (0.0 if step(s, a)[0] == N - 1 else V[step(s, a)[0]]) for a in (-1, 1)}
    policy.append("right" if qs[1] >= qs[-1] else "left")
print("policy:", policy)
