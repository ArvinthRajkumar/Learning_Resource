def seconds(steps, passes, ms_per_call, vae_ms=150, encode_ms=40): return (steps * passes * ms_per_call + vae_ms + encode_ms) / 1000
configs = [("SDXL, 30 steps, CFG", 30, 2, 90), ("SDXL, 20 steps, DPM++, CFG", 20, 2, 90), ("distilled Turbo, 4 steps, no CFG", 4, 1, 90), ("single-step distilled", 1, 1, 90)]
for name, steps, passes, ms in configs:
    print(f"{name:>34}: {seconds(steps, passes, ms):5.2f} s per image on a GPU taking {ms} ms per denoiser call")
