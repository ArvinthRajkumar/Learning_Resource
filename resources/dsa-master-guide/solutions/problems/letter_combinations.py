def letter_combinations(digits):
    if not digits:
        return []
    keys = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    res = []
    def build(i, path):
        if i == len(digits):
            res.append(path)
            return
        for ch in keys[digits[i]]:
            build(i + 1, path + ch)
    build(0, "")
    return res
