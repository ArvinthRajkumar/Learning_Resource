import random
random.seed(2)
def make_image(seed, size=16):
    r = random.Random(seed); return [[r.randint(0, 255) for _ in range(size)] for _ in range(size)]
def downscale(img, size=9):                                    # nearest-neighbour thumbnail to size x size
    n = len(img); return [[img[y * n // size][x * n // size] for x in range(size)] for y in range(size)]
def dhash(img):
    t = downscale(img, 9)
    return [1 if t[y][x] > t[y][x + 1] else 0 for y in range(8) for x in range(8)]       # 64 bits: is the pixel brighter than its right neighbour?
def hamming(a, b): return sum(x != y for x, y in zip(a, b))
original = make_image(1)
brighter = [[min(255, p + 20) for p in row] for row in original]                          # brightness change
noisy = [[max(0, min(255, p + random.randint(-6, 6))) for p in row] for row in original]  # mild recompression-like noise
different = make_image(2)
print("Hamming distance (0 to 64) between 64-bit dHashes:")
print("  original vs brightened:", hamming(dhash(original), dhash(brighter)))
print("  original vs lightly noisy:", hamming(dhash(original), dhash(noisy)))
print("  original vs a different image:", hamming(dhash(original), dhash(different)), "(about 32 for unrelated images)")
