def find_bug_by_bisection(items, is_bad):
    """Binary search for the first bad item, assuming everything after the first bad one is bad (like git bisect)."""
    lo, hi, steps = 0, len(items) - 1, 0
    while lo < hi:
        mid = (lo + hi) // 2; steps += 1
        if is_bad(items[mid]): hi = mid
        else: lo = mid + 1
    return items[lo], steps
commits = list(range(1, 1001))
first_bad, steps = find_bug_by_bisection(commits, lambda c: c >= 637)
print(f"first bad commit: {first_bad}, found in {steps} checks instead of up to 1000")
