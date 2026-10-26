def downtime(avail):
    mins = (1 - avail) * 365 * 24 * 60
    return f"{mins / 60:.1f} h" if mins >= 60 else f"{mins:.1f} min"
for a in (0.99, 0.999, 0.9999, 0.99999):
    print(f"{a * 100:g}% availability -> {downtime(a)} of downtime per year")
# Two components in series, each 99.9% available
print("two 99.9% services in series:", f"{0.999 ** 2:.5f}", "| in parallel (either suffices):", f"{1 - 0.001 ** 2:.6f}")
