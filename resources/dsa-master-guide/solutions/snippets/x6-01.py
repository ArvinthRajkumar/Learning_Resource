import math
print(f"{'n':>8} {'log n':>8} {'n log n':>12} {'n^2':>14} {'2^n':>22}")
for n in [10, 20, 40, 60]:
    print(f"{n:>8} {math.log2(n):>8.1f} {n * math.log2(n):>12.0f} {n * n:>14} {2 ** n:>22}")
