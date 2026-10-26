# Point-in-time correctness: the feature value used for a label must be the latest value BEFORE the label time.
feature_history = [("u1", 10, 5), ("u1", 20, 9), ("u1", 30, 20)]       # (user, timestamp, purchases_30d)
labels = [("u1", 25, 1)]                                                 # (user, label_time, label)
def as_of(user, t):
    vals = [v for u, ts, v in feature_history if u == user and ts <= t]
    return vals[-1] if vals else None
for user, t, y in labels:
    print("label at t=%d uses feature value %s (not the later 20)" % (t, as_of(user, t)))
