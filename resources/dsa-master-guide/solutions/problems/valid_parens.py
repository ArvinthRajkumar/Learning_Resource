def valid_parens(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:                      # closing bracket
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)                 # opening bracket
    return not stack
