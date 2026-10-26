def conv2d(img, kernel):
    kh, kw = len(kernel), len(kernel[0])
    return [[sum(img[i + a][j + b] * kernel[a][b] for a in range(kh) for b in range(kw))
             for j in range(len(img[0]) - kw + 1)] for i in range(len(img) - kh + 1)]
img = [[0, 0, 0, 9, 9],
       [0, 0, 0, 9, 9],
       [0, 0, 0, 9, 9],
       [0, 0, 0, 9, 9]]
vertical_edge = [[-1, 1], [-1, 1]]
for row in conv2d(img, vertical_edge):
    print(row)
n, k, p, s = 32, 3, 1, 1
print("output size:", (n + 2 * p - k) // s + 1, " parameters for 3x3 kernel, 64 in, 128 out channels:", 3 * 3 * 64 * 128 + 128)
