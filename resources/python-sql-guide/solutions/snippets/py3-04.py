def averager():
    total, count, avg = 0.0, 0, None
    while True:
        x = yield avg                # receives values from .send()
        total += x; count += 1
        avg = total / count

g = averager(); next(g)
print(g.send(10), g.send(20), g.send(30))

def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)   # delegate to a sub-generator
        else:
            yield item
print(list(flatten([1, [2, [3, 4]], 5])))
