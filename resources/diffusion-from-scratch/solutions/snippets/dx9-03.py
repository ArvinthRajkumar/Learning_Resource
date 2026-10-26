def shift(t, s): return s * t / (1 + (s - 1) * t)
for s in (1.0, 3.0):
    print(f"shift s = {s}: t = " + ", ".join(f"{t:.1f}->{shift(t, s):.2f}" for t in (0.1, 0.3, 0.5, 0.7, 0.9)))
print("with s = 3 half of the steps (t <= 0.5) are spent where the shifted time is below", round(shift(0.5, 3.0), 2), "that is, there is more emphasis on high-noise levels where global structure forms")
