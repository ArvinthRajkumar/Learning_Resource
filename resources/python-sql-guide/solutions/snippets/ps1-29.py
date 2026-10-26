class C:
    items = []
    count = 0
    def add(self, x):
        self.items.append(x)
        self.count += 1
a, b = C(), C()
a.add(1); b.add(2)
print(a.items, b.items, a.count, b.count, C.count)
