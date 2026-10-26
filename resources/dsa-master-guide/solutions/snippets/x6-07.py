import math, itertools
for n in [4, 8, 16, 64]:
    print(f"n = {n:>3}: ceil(log2(n!)) = {math.ceil(math.log2(math.factorial(n))):>4} comparisons needed at minimum | n log2 n = {n * math.log2(n):.0f}")
def mergesort_compares(a):
    cnt = [0]
    def ms(x):
        if len(x) <= 1: return x
        L, R = ms(x[:len(x)//2]), ms(x[len(x)//2:])
        out, i, j = [], 0, 0
        while i < len(L) and j < len(R):
            cnt[0] += 1
            if L[i] <= R[j]: out.append(L[i]); i += 1
            else: out.append(R[j]); j += 1
        return out + L[i:] + R[j:]
    ms(a); return cnt[0]
worst = max(mergesort_compares(list(p)) for p in itertools.permutations(range(8)))
print("merge sort worst case on 8 items:", worst, "vs information-theoretic minimum", math.ceil(math.log2(math.factorial(8))))
