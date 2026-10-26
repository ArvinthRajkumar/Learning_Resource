class TicTacToe:
    def __init__(self, n): self.n, self.rows, self.cols, self.diag, self.anti = n, [0] * n, [0] * n, 0, 0
    def move(self, r, c, player):
        v = 1 if player == 1 else -1
        self.rows[r] += v; self.cols[c] += v
        if r == c: self.diag += v
        if r + c == self.n - 1: self.anti += v
        n = self.n
        return player if n in (abs(self.rows[r]), abs(self.cols[c]), abs(self.diag), abs(self.anti)) else 0
g = TicTacToe(3)
results = [g.move(0, 0, 1), g.move(0, 2, 2), g.move(2, 2, 1), g.move(1, 1, 2), g.move(2, 0, 1), g.move(1, 0, 2), g.move(2, 1, 1)]
print(results, "| player 1 wins on the last move by completing the bottom row" if results[-1] == 1 else "")
