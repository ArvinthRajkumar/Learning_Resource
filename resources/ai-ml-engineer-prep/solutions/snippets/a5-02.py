d, layers = 4096, 32
params = layers * 12 * d * d
print("approx parameters from the formula: %.2f B" % (params / 1e9))
for n in (2_048, 8_192, 32_768, 131_072):
    entries = n * n
    print("n=%7d: score matrix per head %.2e entries = %.1f GB in fp16 per head if materialised" % (n, entries, entries * 2 / 1e9))
