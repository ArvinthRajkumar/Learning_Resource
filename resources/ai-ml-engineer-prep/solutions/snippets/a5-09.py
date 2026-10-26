params = 70e9
for name, bits in (("fp16/bf16", 16), ("int8", 8), ("int4", 4)):
    print("%-10s %6.0f GB for weights of a 70B model" % (name, params * bits / 8 / 1e9))
