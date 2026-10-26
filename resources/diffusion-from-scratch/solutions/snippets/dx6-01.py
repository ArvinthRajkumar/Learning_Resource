frames, seconds, fps = 16, 5, 24
latent_per_frame = 64 * 64 * 4
print("latent values for a 5 s clip at 24 fps:", seconds * fps * latent_per_frame)
print("a 16-frame clip:", frames * latent_per_frame)
print("naive full attention between all positions in 16 frames:", (frames * 64 * 64) ** 2)
