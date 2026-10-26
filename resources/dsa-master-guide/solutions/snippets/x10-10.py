import itertools
LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
def winner(b):
    for a, c, d in LINES:
        if b[a] != " " and b[a] == b[c] == b[d]: return b[a]
    return None
nodes = {"plain": 0, "alpha_beta": 0}
def minimax(b, player):                                               # returns +1 if X wins, -1 if O wins, 0 draw
    nodes["plain"] += 1
    w = winner(b)
    if w: return 1 if w == "X" else -1
    if " " not in b: return 0
    vals = [minimax(b[:i] + player + b[i + 1:], "O" if player == "X" else "X") for i in range(9) if b[i] == " "]
    return max(vals) if player == "X" else min(vals)
def alphabeta(b, player, alpha=-2, beta=2):
    nodes["alpha_beta"] += 1
    w = winner(b)
    if w: return 1 if w == "X" else -1
    if " " not in b: return 0
    if player == "X":
        best = -2
        for i in range(9):
            if b[i] == " ":
                best = max(best, alphabeta(b[:i] + "X" + b[i + 1:], "O", alpha, beta)); alpha = max(alpha, best)
                if alpha >= beta: break
        return best
    best = 2
    for i in range(9):
        if b[i] == " ":
            best = min(best, alphabeta(b[:i] + "O" + b[i + 1:], "X", alpha, beta)); beta = min(beta, best)
            if alpha >= beta: break
    return best
start = "         "
v1, v2 = minimax(start, "X"), alphabeta(start, "X")
print("value of tic-tac-toe with perfect play (0 = draw):", v1, v2, "| same answer:", v1 == v2)
print(f"positions examined: plain minimax {nodes['plain']:,} vs alpha-beta {nodes['alpha_beta']:,}")
