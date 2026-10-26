import struct
def to_bf16(x):                                             # keep the top 16 bits of the float32 representation (truncation)
    bits = struct.unpack(">I", struct.pack(">f", x))[0] & 0xFFFF0000
    return struct.unpack(">f", struct.pack(">I", bits))[0]
def to_fp16(x):
    try: return struct.unpack(">e", struct.pack(">e", x))[0]
    except OverflowError: return float("inf")
for x in (3.14159265, 1e-8, 70000.0, 0.1):
    print(f"{x!r:>12}: bf16 {to_bf16(x)!r:>14} | fp16 {to_fp16(x)!r:>14}")
print("fp16 overflows above 65504 and flushes tiny gradients toward zero, which is why it needs loss scaling; bf16 keeps the range but loses precision")
