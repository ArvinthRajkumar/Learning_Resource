steps = 30
for strength in (0.2, 0.5, 0.8, 1.0):
    run = int(steps * strength)
    print("strength %.1f -> start at step %2d, run %2d denoising steps (%.0f%% of full cost)" % (strength, steps - run, run, 100 * run / steps))
