for p in (4, 8):
    print(f"{p} pipeline stages: " + " | ".join(f"{m} micro-batches -> bubble {(p - 1) / (m + p - 1):.0%}" for m in (4, 16, 64)))
