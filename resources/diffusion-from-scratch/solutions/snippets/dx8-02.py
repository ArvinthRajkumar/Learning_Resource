def cfg(eps_uncond, eps_cond, w): return [u + w * (c - u) for u, c in zip(eps_uncond, eps_cond)]
u, c = [0.10, -0.20, 0.05], [0.30, -0.10, 0.25]
for w in (0, 1, 3, 7.5, 15):
    print(f"guidance {w:>4}: {[round(v, 2) for v in cfg(u, c, w)]}  (0 ignores the prompt, 1 is the plain conditional prediction, larger exaggerates the prompt direction)")
steps, cost_per_call = 25, 1.0
print(f"cost: with guidance every step needs 2 denoiser calls -> {2 * steps} calls instead of {steps}; distilled or guidance-free models skip the second call")
