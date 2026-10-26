for name, params in (("U-Net", 860e6), ("text encoder", 123e6), ("VAE", 84e6)):
    print("%-13s %.2f GB in fp16, %.2f GB in fp32" % (name, params * 2 / 1e9, params * 4 / 1e9))
print("total fp16: %.2f GB" % ((860e6 + 123e6 + 84e6) * 2 / 1e9))
