import random

class RandomizedSet:
    def __init__(self):
        self.items, self.pos = [], {}

    def insert(self, val):
        if val in self.pos:
            return False
        self.pos[val] = len(self.items)
        self.items.append(val)
        return True

    def remove(self, val):
        if val not in self.pos:
            return False
        i, last = self.pos[val], self.items[-1]
        self.items[i], self.pos[last] = last, i    # move the last item into the hole
        self.items.pop()
        del self.pos[val]
        return True

    def get_random(self):
        return random.choice(self.items)
