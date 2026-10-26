d_in = d_out = 1024
for r in (4, 8, 32, 128):
    lora = r * (d_in + d_out)
    full = d_in * d_out
    print("rank %3d: %7d params vs %8d full (%.1f%%)" % (r, lora, full, 100 * lora / full))

# a whole U-Net: suppose 160 attention matrices of about 1024 x 1024
mats, r = 160, 8
print("rank-8 LoRA over", mats, "matrices:", mats * r * 2 * 1024, "params =", round(mats * r * 2 * 1024 * 2 / 1e6, 1), "MB in fp16")
