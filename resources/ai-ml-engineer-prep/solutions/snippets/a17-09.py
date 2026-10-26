import math
for C in (1e21, 1e23, 1e25):
    N_opt = math.sqrt(C / 120); D_opt = 20 * N_opt
    print(f"compute {C:.0e} FLOPs: compute-optimal about {N_opt / 1e9:7.1f}B parameters trained on {D_opt / 1e12:6.2f}T tokens")
print("A 7B model trained on 2T tokens uses", round(2e12 / 7e9), "tokens per parameter, far beyond 20: 'over-training' makes a smaller model that is cheaper to serve")
