import math, random

class V:
    def __init__(self, data, parents=()):
        self.data, self.grad, self._parents, self._backward = data, 0.0, parents, lambda: None
    def __add__(self, o):
        o = o if isinstance(o, V) else V(o)
        out = V(self.data + o.data, (self, o))
        def bw():
            self.grad += out.grad
            o.grad += out.grad
        out._backward = bw
        return out
    def __mul__(self, o):
        o = o if isinstance(o, V) else V(o)
        out = V(self.data * o.data, (self, o))
        def bw():
            self.grad += o.data * out.grad
            o.grad += self.data * out.grad
        out._backward = bw
        return out
    __radd__ = __add__
    __rmul__ = __mul__
    def __neg__(self): return self * -1
    def __sub__(self, o): return self + (-o if isinstance(o, V) else V(-o))
    def tanh(self):
        t = math.tanh(self.data)
        out = V(t, (self,))
        def bw(): self.grad += (1 - t * t) * out.grad
        out._backward = bw
        return out
    def backward(self):
        order, seen = [], set()
        def visit(v):
            if v not in seen:
                seen.add(v)
                for p in v._parents: visit(p)
                order.append(v)
        visit(self)
        self.grad = 1.0
        for v in reversed(order): v._backward()

random.seed(1)
class Neuron:
    def __init__(self, n_in):
        self.w = [V(random.uniform(-1, 1)) for _ in range(n_in)]
        self.b = V(0.0)
    def __call__(self, x):
        return (sum((wi * xi for wi, xi in zip(self.w, x)), self.b)).tanh()
    def params(self): return self.w + [self.b]
class MLP:
    def __init__(self, sizes):
        self.layers = [[Neuron(sizes[i]) for _ in range(sizes[i + 1])] for i in range(len(sizes) - 1)]
    def __call__(self, x):
        for layer in self.layers:
            x = [n(x) for n in layer]
        return x[0]
    def params(self): return [p for layer in self.layers for n in layer for p in n.params()]

net = MLP([2, 4, 1])
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [-1, 1, 1, -1]                         # XOR with targets in {-1, +1}
for epoch in range(301):
    loss = sum(((net(x) - y) * (net(x) - y) for x, y in zip(X, Y)), V(0.0))
    for p in net.params(): p.grad = 0.0
    loss.backward()
    for p in net.params(): p.data -= 0.05 * p.grad
    if epoch in (0, 100, 300):
        print("epoch %3d loss %.4f" % (epoch, loss.data))
print([round(net(x).data, 2) for x in X], "targets", Y)
