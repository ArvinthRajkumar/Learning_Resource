import random
random.seed(7)
n, k = 20, 5
idx = list(range(n)); random.shuffle(idx)
folds = [idx[i::k] for i in range(k)]
for i, test in enumerate(folds):
    train = [j for f in folds[:i] + folds[i + 1:] for j in f]
    print("fold", i, "train", len(train), "test", len(test), "disjoint:", not set(train) & set(test))
