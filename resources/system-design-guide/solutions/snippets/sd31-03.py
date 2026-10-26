class Auction:
    def __init__(self, end, increment=5, snipe_window=60, extension=120):
        self.end, self.inc, self.win, self.ext = end, increment, snipe_window, extension
        self.high, self.leader, self.history = 0, None, []
    def bid(self, user, amount, now):                       # processed by one writer, in order
        if now >= self.end: return "rejected: auction ended"
        if amount < self.high + self.inc: return f"rejected: need at least {self.high + self.inc}"
        self.high, self.leader = amount, user
        self.history.append((now, user, amount))
        if self.end - now <= self.win:                      # anti-sniping
            self.end = now + self.ext
            return f"accepted, end extended to {self.end}"
        return "accepted"
a = Auction(end=1000)
for t, u, amt in [(100, "ana", 50), (200, "bo", 52), (300, "bo", 60), (950, "cy", 70), (1030, "ana", 75), (1160, "di", 90), (1200, "bo", 95)]:
    print(f"t={t:>4} {u}: {amt:>3} -> {a.bid(u, amt, t)}")
print("winner:", a.leader, "at", a.high, "| bids recorded:", len(a.history))
