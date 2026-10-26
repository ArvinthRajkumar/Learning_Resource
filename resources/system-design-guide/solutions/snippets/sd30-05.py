# The load generator intends to send one request every 10 ms. The server is normally instant,
# except for one 10-second stall that begins at t = 5 s.
interval, total_ms, stall_start, stall_end = 10, 20_000, 5_000, 15_000
def server_latency_at(t):
    return (stall_end - t) + 1 if stall_start <= t < stall_end else 1          # a request during the stall waits for it to end
# Closed loop: the client sends the next request only after the previous reply arrives
closed, t = [], 0
while t < total_ms:
    lat = server_latency_at(t); closed.append(lat); t += max(lat, interval)
# Open loop: requests are issued on schedule whatever the server is doing, like real arriving users
open_loop = [server_latency_at(t) for t in range(0, total_ms, interval)]
def pct(xs, p): return sorted(xs)[int(len(xs) * p / 100)]
print(f"closed loop: {len(closed):>5} samples, p50 {pct(closed, 50)} ms, p99 {pct(closed, 99)} ms")
print(f"open loop  : {len(open_loop):>5} samples, p50 {pct(open_loop, 50)} ms, p99 {pct(open_loop, 99)} ms")
