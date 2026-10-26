events = [(1, "a"), (3, "a"), (4, "b"), (11, "a"), (2, "b"), (12, "b"), (25, "a"), (5, "a")]   # (event_time, key); some arrive out of order
WINDOW, LATENESS = 10, 3
windows, watermark, emitted, late = {}, 0, [], []
for t, k in events:
    w = t // WINDOW * WINDOW
    if w + WINDOW <= watermark - LATENESS:
        late.append((t, k)); continue
    windows.setdefault(w, {}); windows[w][k] = windows[w].get(k, 0) + 1
    watermark = max(watermark, t)
    for ws in sorted(list(windows)):
        if ws + WINDOW <= watermark - LATENESS:
            emitted.append((ws, windows.pop(ws)))
print("emitted windows:", emitted)
print("still open:", windows, "| dropped as too late:", late)
