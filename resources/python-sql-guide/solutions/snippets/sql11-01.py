import random
random.seed(1)
R = [(i, f"r{i}") for i in random.sample(range(10_000), 2_000)]          # (key, payload)
S = [(i, f"s{i}") for i in random.sample(range(10_000), 3_000)]
def nested_loop(R, S):
    out, comparisons = [], 0
    for rk, rv in R:
        for sk, sv in S:
            comparisons += 1
            if rk == sk: out.append((rk, rv, sv))
    return out, comparisons
def hash_join(R, S):
    table, out, ops = {}, [], 0
    for sk, sv in S: table.setdefault(sk, []).append(sv); ops += 1                 # build on one side
    for rk, rv in R:
        ops += 1
        for sv in table.get(rk, ()): out.append((rk, rv, sv))                        # probe with the other
    return out, ops
def merge_join(R, S):
    R, S = sorted(R), sorted(S); i = j = ops = 0; out = []
    while i < len(R) and j < len(S):
        ops += 1
        if R[i][0] < S[j][0]: i += 1
        elif R[i][0] > S[j][0]: j += 1
        else:
            out.append((R[i][0], R[i][1], S[j][1])); i += 1; j += 1                     # keys are unique here
    return out, ops
nl, c1 = nested_loop(R, S); hj, c2 = hash_join(R, S); mj, c3 = merge_join(R, S)
print("all three return the same rows:", sorted(nl) == sorted(hj) == sorted(mj), "| result size:", len(hj))
print(f"basic operations: nested loop {c1:,} | hash join {c2:,} | merge join {c3:,} (after sorting)")
