def training_estimate(params, tokens, gpus, peak_tflops, mfu, price_per_gpu_hour):
    flops = 6 * params * tokens
    seconds = flops / (gpus * peak_tflops * 1e12 * mfu)
    gpu_hours = gpus * seconds / 3600
    return flops, seconds / 86400, gpu_hours, gpu_hours * price_per_gpu_hour
for name, N_, D_, g in [("1B model, 20B tokens", 1e9, 20e9, 8), ("7B model, 1T tokens", 7e9, 1e12, 512), ("70B model, 2T tokens", 70e9, 2e12, 2048)]:
    flops, days, gh, cost = training_estimate(N_, D_, g, peak_tflops=312, mfu=0.4, price_per_gpu_hour=2.0)      # an A100-class GPU, bf16 peak 312 TFLOP/s
    print(f"{name:>22}: {flops:.2e} FLOPs | {g:>4} GPUs -> {days:7.1f} days | {gh:>11,.0f} GPU-hours | about ${cost:>12,.0f} at $2/GPU-hour")
