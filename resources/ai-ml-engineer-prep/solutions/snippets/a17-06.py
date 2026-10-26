def zero_memory_gb(params, p, stage):
    psi = params
    per_param = {0: 16, 1: 4 + 12 / p, 2: 2 + 14 / p, 3: 16 / p}[stage]
    return psi * per_param / 1e9
for stage in (0, 1, 2, 3):
    print(f"7B model on 8 GPUs, ZeRO stage {stage}: {zero_memory_gb(7e9, 8, stage):6.1f} GB of model state per GPU" + ("   (fits in 80 GB)" if zero_memory_gb(7e9, 8, stage) < 60 else "   (does not fit in 80 GB with activations)"))
print("70B model on 64 GPUs, ZeRO-3:", round(zero_memory_gb(70e9, 64, 3), 1), "GB per GPU")
