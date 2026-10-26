f = lambda x: x ** 3 - 2 * x
fprime = lambda x: 3 * x ** 2 - 2
x, h = 1.5, 1e-6
numeric = (f(x + h) - f(x - h)) / (2 * h)       # central difference
print("analytic", fprime(x), "numeric", round(numeric, 6))
