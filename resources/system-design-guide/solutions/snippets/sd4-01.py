import math
for n in (10**6, 10**9, 10**12):
    print(n, "keys, fan-out 200 -> depth", math.ceil(math.log(n, 200)))
