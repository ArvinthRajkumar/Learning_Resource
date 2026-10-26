squares = [n * n for n in range(6)]
evens = [n for n in range(10) if n % 2 == 0]
pairs = [(x, y) for x in range(3) for y in range(2) if x != y]
lens = {w: len(w) for w in ["a", "bb", "ccc"]}
uniq = {n % 3 for n in range(10)}
print(squares, evens, pairs, lens, uniq, sep="\n")
