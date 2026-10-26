import bisect
history = {"u1": [(1, 3), (5, 7), (9, 12)]}          # user_id -> [(timestamp, purchases_so_far)]
def feature_at(user, t):
    ts = [x[0] for x in history[user]]
    i = bisect.bisect_right(ts, t) - 1
    return history[user][i][1] if i >= 0 else 0
for event_time in (4, 5, 8, 10):
    print(f"label at t={event_time}: feature value known then = {feature_at('u1', event_time)} (using the latest value, 12, would leak the future)")
