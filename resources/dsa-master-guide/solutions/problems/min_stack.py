class MinStack:
    def __init__(self):
        self.data = []                       # (value, min so far)

    def push(self, x):
        lowest = min(x, self.data[-1][1]) if self.data else x
        self.data.append((x, lowest))

    def pop(self):
        return self.data.pop()[0]

    def top(self):
        return self.data[-1][0]

    def get_min(self):
        return self.data[-1][1]
