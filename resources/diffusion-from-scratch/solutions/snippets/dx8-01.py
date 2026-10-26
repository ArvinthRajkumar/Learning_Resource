def latent_shape(width, height, channels=4, factor=8): return (channels, height // factor, width // factor)
def latent_elements(width, height, channels=4): c, h, w = latent_shape(width, height, channels); return c * h * w
for w, h in [(512, 512), (768, 768), (1024, 1024), (1536, 1024)]:
    c, lh, lw = latent_shape(w, h)
    print(f"{w}x{h} image -> latent {c}x{lh}x{lw} = {latent_elements(w, h):,} numbers ({w * h * 3 / latent_elements(w, h):.0f}x fewer than the pixels)")
