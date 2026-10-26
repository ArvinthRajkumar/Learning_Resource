import random
random.seed(7)
def backoff(attempt, base=0.1, cap=5.0):
    return random.uniform(0, min(cap, base * 2 ** attempt))   # "full jitter"
print([round(backoff(a), 2) for a in range(8)])
