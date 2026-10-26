def flatten(items):
    for x in items:
        if isinstance(x, (list, tuple)):
            yield from flatten(x)
        else:
            yield x
print(list(flatten([1, [2, (3, [4])], 5, [[6]]])))
