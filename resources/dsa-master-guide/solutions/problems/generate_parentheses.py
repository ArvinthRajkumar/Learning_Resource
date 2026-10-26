def generate_parentheses(n):
    res = []
    def backtrack(cur, opens, closes):
        if len(cur) == 2 * n:
            res.append(cur)
            return
        if opens < n:
            backtrack(cur + "(", opens + 1, closes)
        if closes < opens:
            backtrack(cur + ")", opens, closes + 1)
    backtrack("", 0, 0)
    return res
