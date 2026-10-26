def countdown(n):
    while n > 0:
        yield n                 # pause here and hand back one value
        n -= 1
it = countdown(3)
print(next(it), next(it), next(it), "| then:", list(it), "(already exhausted)")
