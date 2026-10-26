def weights_gb(params, bytes_per): return params * bytes_per / 1e9
models = {"SD 1.5 U-Net (0.86B)": 0.86e9, "SDXL U-Net (2.6B)": 2.6e9, "SD3 / Flux-class DiT (about 12B)": 12e9, "T5-XXL text encoder (4.7B)": 4.7e9}
print(f"{'component':>34} {'fp32':>7} {'fp16':>7} {'8-bit':>7} {'4-bit':>7}")
for name, p in models.items():
    print(f"{name:>34} {weights_gb(p, 4):>6.1f}G {weights_gb(p, 2):>6.1f}G {weights_gb(p, 1):>6.1f}G {weights_gb(p, 0.5):>6.1f}G")
print("a 12B DiT in fp16 needs about", weights_gb(12e9, 2), "GB for weights alone, so consumer GPUs use 8-bit/4-bit weights and offload the text encoder")
