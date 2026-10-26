from collections import deque
stock, queue, rejected = 10, deque(), 0
requests = 40                                       # arrive in a burst
for user in range(requests):
    if stock > 0:                                   # in production: one atomic Redis DECR / Lua script
        stock -= 1
        queue.append(f"user{user}")                 # winners get a reservation and go on to pay
    else:
        rejected += 1                               # everyone else is turned away cheaply at the edge
print(f"{requests} requests -> {len(queue)} reservations queued, {rejected} rejected without touching the database, stock left {stock}")
