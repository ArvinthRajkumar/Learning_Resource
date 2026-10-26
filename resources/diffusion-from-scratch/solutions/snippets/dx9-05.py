def dit_stats(width, layers, tokens, mlp_ratio=4):
    params_per_layer = (4 + 2 * mlp_ratio) * width * width + 6 * width * width      # attention (4w^2) + MLP (2*r*w^2) + adaLN modulation (6w^2)
    params = layers * params_per_layer
    flops_forward = 2 * params * tokens + layers * 4 * tokens * tokens * width        # matmuls + attention score and value products
    return params, flops_forward
for name, w, L in [("DiT-S", 384, 12), ("DiT-B", 768, 12), ("DiT-XL", 1152, 28), ("a 12B-class model", 4096, 48)]:
    p, f = dit_stats(w, L, tokens=4096)
    print(f"{name:>18}: about {p / 1e9:6.2f}B parameters | one forward pass over 4096 tokens: {f / 1e12:7.2f} TFLOPs | 30 steps with CFG: {60 * f / 1e12:8.0f} TFLOPs per image")
