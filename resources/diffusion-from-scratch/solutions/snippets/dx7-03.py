import struct
def to_fp16(x):
    return struct.unpack("e", struct.pack("e", x))[0]
grad = 1e-8
print("fp16 of tiny gradient     :", to_fp16(grad))
scale = 1024.0
scaled = to_fp16(grad * scale)
print("fp16 of scaled gradient   :", scaled)
print("recovered after unscaling :", scaled / scale)
print("fp16 largest finite value :", to_fp16(65504.0), " overflow ->", end=" ")
try:
    print(to_fp16(70000.0))
except OverflowError:
    print("OverflowError")
