a, b = 17, 5
print(a // b, a % b, a / b, a ** 2)      # 3 2 3.4 289
print(divmod(a, b))                       # (3, 2)
print(abs(-4), min(3, 9), max(3, 9), round(2.567, 2))
s = "infosys"
print(s.upper(), s[0], s[-1], s[1:4], len(s))
nums = [4, 1, 3]
nums.append(9); nums.sort(); print(nums)   # [1, 3, 4, 9]
d = {"a": 1}; d["b"] = 2; print(d.get("c", 0))   # 0
