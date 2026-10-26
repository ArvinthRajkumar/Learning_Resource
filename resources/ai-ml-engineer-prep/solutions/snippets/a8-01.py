# Receptive field growth: each layer with kernel k and stride s adds (k - 1) * product of earlier strides.
layers = [(3, 1), (3, 1), (3, 2), (3, 1), (3, 2)]       # (kernel, stride)
rf, jump = 1, 1
for i, (k, s) in enumerate(layers, 1):
    rf += (k - 1) * jump
    jump *= s
    print("after layer %d: receptive field %dx%d" % (i, rf, rf))
