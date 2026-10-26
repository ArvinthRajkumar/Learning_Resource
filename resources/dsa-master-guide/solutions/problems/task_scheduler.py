from collections import Counter

def task_scheduler(tasks, n):
    counts = Counter(tasks).values()
    most = max(counts)
    with_most = sum(1 for c in counts if c == most)
    return max(len(tasks), (most - 1) * (n + 1) + with_most)
