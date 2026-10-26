def multiply_strings(a, b):
    if a == "0" or b == "0":
        return "0"
    res = [0] * (len(a) + len(b))
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            total = int(a[i]) * int(b[j]) + res[i + j + 1]
            res[i + j + 1] = total % 10
            res[i + j] += total // 10
    return "".join(map(str, res)).lstrip("0")
