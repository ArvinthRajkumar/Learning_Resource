def n_per_group(p, mde, z_alpha=1.96, z_beta=0.84):
    return int(2 * (z_alpha + z_beta) ** 2 * p * (1 - p) / mde ** 2) + 1
for mde in (0.02, 0.01, 0.005):
    print("baseline 10%%, detect %.1f point lift: %d users per group" % (mde * 100, n_per_group(0.10, mde)))
