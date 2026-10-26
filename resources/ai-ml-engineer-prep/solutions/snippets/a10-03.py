import random
random.seed(0)
# Gridworld 4 wide, 3 tall. Start (0,0). Goal (3,2) gives +1. Pit (3,1) gives -1. Both end the episode. Step cost -0.04.
W, H = 4, 3
GOAL, PIT = (3, 2), (3, 1)
actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]              # up, down, right, left (y up)
def move(s, a):
    x, y = s[0] + a[0], s[1] + a[1]
    if not (0 <= x < W and 0 <= y < H): x, y = s
    return (x, y)
Q = {((x, y), a): 0.0 for x in range(W) for y in range(H) for a in range(4)}
alpha, gamma, eps = 0.2, 0.95, 0.2
for episode in range(5000):
    s = (0, 0)
    for _ in range(100):
        a = random.randrange(4) if random.random() < eps else max(range(4), key=lambda i: Q[(s, i)])
        s2 = move(s, actions[a])
        r = 1.0 if s2 == GOAL else -1.0 if s2 == PIT else -0.04
        done = s2 in (GOAL, PIT)
        target = r + (0 if done else gamma * max(Q[(s2, i)] for i in range(4)))
        Q[(s, a)] += alpha * (target - Q[(s, a)])
        s = s2
        if done: break
arrows = "^v><"
for y in reversed(range(H)):
    print(" ".join("G" if (x, y) == GOAL else "X" if (x, y) == PIT else arrows[max(range(4), key=lambda i: Q[((x, y), i)])] for x in range(W)))
