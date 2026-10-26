pixels = 512 * 512 * 3
latent = 64 * 64 * 4
print(f"a 512x512 RGB image has {pixels:,} numbers; its latent has {latent:,} ({pixels / latent:.0f}x fewer), so every denoising step is about {pixels / latent:.0f}x cheaper")
