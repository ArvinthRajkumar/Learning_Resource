import bisect
class Leaderboard:
    """Sorted list stand-in for a Redis sorted set (insert O(n) here, O(log n) in Redis)."""
    def __init__(self):
        self.items = []                 # sorted ascending by (score, player)
        self.score = {}
    def update(self, player, score):
        if player in self.score:
            self.items.remove((self.score[player], player))
        bisect.insort(self.items, (score, player))
        self.score[player] = score
    def top(self, n):
        return [(p, s) for s, p in reversed(self.items[-n:])]
    def rank(self, player):             # 1-based, highest score is rank 1
        i = self.items.index((self.score[player], player))
        return len(self.items) - i

lb = Leaderboard()
for p, s in [("ann", 50), ("bob", 80), ("cy", 65), ("di", 90)]:
    lb.update(p, s)
lb.update("ann", 85)
print(lb.top(3), lb.rank("bob"), lb.rank("ann"))
