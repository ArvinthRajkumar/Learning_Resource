from collections import deque
class Snake:
    DIRS = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    def __init__(self, h, w, food):
        self.h, self.w, self.food, self.body, self.cells, self.score = h, w, deque(food), deque([(0, 0)]), {(0, 0)}, 0
    def move(self, d):
        r, c = self.body[-1]; dr, dc = self.DIRS[d]; nr, nc = r + dr, c + dc
        if not (0 <= nr < self.h and 0 <= nc < self.w): return -1                        # hit the wall
        eating = bool(self.food) and tuple(self.food[0]) == (nr, nc)
        if not eating:
            self.cells.discard(self.body.popleft())                                       # tail moves away first
        elif self.food: self.food.popleft(); self.score += 1
        if (nr, nc) in self.cells: return -1                                              # hit itself
        self.body.append((nr, nc)); self.cells.add((nr, nc))
        return self.score
g = Snake(4, 4, [(0, 1), (0, 2), (0, 3), (1, 3)])
print("scores after each move (the snake grows by eating the 4 food items, then turns back on itself):", [g.move(d) for d in "RRRDLU"], "| -1 means game over")
g2 = Snake(2, 2, []); print("wall collision:", [g2.move(d) for d in "RRR"])
