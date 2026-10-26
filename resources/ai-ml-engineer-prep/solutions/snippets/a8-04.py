def dice(a, b):
    inter = sum(x and y for x, y in zip(a, b))
    return 2 * inter / (sum(a) + sum(b))
pred = [1, 1, 1, 0, 0, 0, 0, 1]
true = [1, 1, 0, 0, 0, 1, 0, 1]
inter = sum(p and t for p, t in zip(pred, true))
union = sum(p or t for p, t in zip(pred, true))
print("IoU %.3f, Dice %.3f" % (inter / union, dice(pred, true)))
