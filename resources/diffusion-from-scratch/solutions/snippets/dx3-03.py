# DiT token counts: a 1024 px image, latent 128 x 128 x 16 channels, patch size 2
side, patch = 128, 2
tokens = (side // patch) ** 2
print("tokens per image:", tokens)
print("self-attention score matrix per head per layer:", tokens * tokens, "entries")
