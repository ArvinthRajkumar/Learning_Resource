# A tiny linear recurrence: fixed-size state regardless of sequence length.
A, B, C = 0.9, 1.0, 1.0
h, outs = 0.0, []
for x in [1, 0, 0, 0, 0, 2, 0, 0]:
    h = A * h + B * x
    outs.append(round(C * h, 3))
print(outs)
