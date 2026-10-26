def fanout_cost(members, online_fraction, gateways=200):
    online = int(members * online_fraction)
    per_member_queue = members                                # naive: one queue write per member
    per_gateway = min(gateways, online)                       # gateway-level pub/sub: one message per gateway with a subscriber
    return per_member_queue, per_gateway
for members in (50, 5_000, 500_000):
    naive, smart = fanout_cost(members, 0.2)
    print(f"channel of {members:>7,} members: naive {naive:>7,} queue writes vs {smart:>3} gateway publishes per message")
