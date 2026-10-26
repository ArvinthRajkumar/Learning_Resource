pixel = 512 * 512 * 3
latent = 64 * 64 * 4
print("pixel values:", pixel, " latent values:", latent, " ratio: %.0fx fewer" % (pixel / latent))
tokens_pixel, tokens_latent = 512 * 512, 64 * 64
print("attention pairs ratio: %.0fx fewer" % ((tokens_pixel / tokens_latent) ** 2))
for size in (256, 512, 768, 1024):
    side = size // 8
    print(size, "px image -> latent", side, "x", side, "x 4 =", side * side * 4, "values")
