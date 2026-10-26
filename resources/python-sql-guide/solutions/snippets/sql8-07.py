def find_deadlock(waits_for):
    """waits_for: {transaction: transaction it waits for}. Returns a cycle if any."""
    for start in waits_for:
        seen, cur = [], start
        while cur in waits_for and cur not in seen:
            seen.append(cur); cur = waits_for[cur]
        if cur in seen:
            return seen[seen.index(cur):] + [cur]
    return None
print("T1 waits for T2, T2 waits for T1:", find_deadlock({"T1": "T2", "T2": "T1"}))
print("T1 waits for T2, T2 waits for T3:", find_deadlock({"T1": "T2", "T2": "T3"}))
