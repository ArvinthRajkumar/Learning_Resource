import random
random.seed(2)
def applicants(n):
    rows = []
    for _ in range(n):
        g = random.choice("AB")
        skill = random.gauss(0, 1) + (0.0 if g == "A" else -0.5)                       # historical disadvantage lowers B's measured score
        qualified = skill + random.gauss(0, 0.7) > 0.3 if g == "A" else skill + 0.5 + random.gauss(0, 0.7) > 0.3     # same true qualification rule
        rows.append((g, skill, qualified))
    return rows
data = applicants(20000)
def report(threshold_for):
    out = {}
    for g in "AB":
        grp = [(s, q) for gg, s, q in data if gg == g]
        pred = [(s > threshold_for[g], q) for s, q in grp]
        sel = sum(p for p, _ in pred) / len(pred)
        tpr = sum(p and q for p, q in pred) / max(1, sum(q for _, q in pred))
        fpr = sum(p and not q for p, q in pred) / max(1, sum(not q for _, q in pred))
        out[g] = (sel, tpr, fpr)
    return out
for name, th in [("one threshold (0.3)", {"A": 0.3, "B": 0.3}), ("group-specific thresholds", {"A": 0.3, "B": -0.2})]:
    r = report(th)
    print(f"{name:>26}: " + " | ".join(f"group {g}: selected {r[g][0]:.2f}, TPR {r[g][1]:.2f}, FPR {r[g][2]:.2f}" for g in "AB"))
