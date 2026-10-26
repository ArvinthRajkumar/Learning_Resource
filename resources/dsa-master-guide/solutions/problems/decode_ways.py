def decode_ways(s):
    if not s or s[0] == "0":
        return 0
    prev, cur = 1, 1                       # ways for 0 digits and 1 digit
    for i in range(1, len(s)):
        new = 0
        if s[i] != "0":
            new += cur                      # decode s[i] alone
        if 10 <= int(s[i - 1:i + 1]) <= 26:
            new += prev                     # decode the pair
        prev, cur = cur, new
    return cur
