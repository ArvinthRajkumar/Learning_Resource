def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
c1, c2 = make_counter(), make_counter()
print(c1(), c1(), c2())

# late binding gotcha: all lambdas see the final i
fs = [lambda: i for i in range(3)]
print([f() for f in fs])
fs = [lambda i=i: i for i in range(3)]      # bind the current value
print([f() for f in fs])
