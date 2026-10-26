def tokens(width, height, patch=2, factor=8): return (width // factor // patch) * (height // factor // patch)      # DiT-style latent patches
base = tokens(512, 512)
for w, h in [(512, 512), (768, 768), (1024, 1024), (2048, 2048)]:
    t = tokens(w, h)
    print(f"{w}x{h}: {t:>6,} tokens | attention cost relative to 512x512: {(t / base) ** 2:>7.0f}x | linear parts: {t / base:>4.0f}x")
