side, patch, d = 224, 16, 768
tokens = (side // patch) ** 2
print("patches per image:", tokens, "; with [CLS]:", tokens + 1)
print("attention score matrix entries per head:", (tokens + 1) ** 2)
print("patch embedding parameters:", patch * patch * 3 * d)
