def mfu(tokens_per_sec, params, gpus, peak_tflops): return tokens_per_sec * 6 * params / (gpus * peak_tflops * 1e12)
for label, tps in [("untuned baseline", 9_000), ("after fused kernels and data fixes", 21_000), ("well-tuned", 34_000)]:
    print(f"{label:>34}: {tps:>6} tokens/s on 8 GPUs training a 7B model -> MFU {mfu(tps, 7e9, 8, 312):.0%}")
