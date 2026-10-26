import heapq

class MinHeap:
    def __init__(self):
        self.a = []

    def push(self, x):
        a = self.a
        a.append(x)
        i = len(a) - 1
        while i > 0 and a[(i - 1) // 2] > a[i]:     # sift up
            a[(i - 1) // 2], a[i] = a[i], a[(i - 1) // 2]
            i = (i - 1) // 2

    def pop(self):
        a = self.a
        top, a[0] = a[0], a[-1]
        a.pop()
        i = 0
        while True:                                  # sift down
            small, l, r = i, 2 * i + 1, 2 * i + 2
            if l < len(a) and a[l] < a[small]: small = l
            if r < len(a) and a[r] < a[small]: small = r
            if small == i:
                return top
            a[i], a[small] = a[small], a[i]
            i = small

h = [5, 1, 8, 3]
heapq.heapify(h)               # O(n)
smallest = heapq.heappop(h)    # 1
