import random
random.seed(7)
def all_subsets_of(mask):
    sub, out = mask, []
    while True:
        out.append(sub)
        if sub == 0: break
        sub = (sub - 1) & mask
    return out
mask = 0b10110
subs = all_subsets_of(mask)
print("submasks of", bin(mask), ":", [bin(s) for s in sorted(subs)], "| count 2^popcount:", len(subs) == 2 ** mask.bit_count())
nums = [4, 1, 2, 1, 2, 7, 4]
single = 0
for x in nums: single ^= x
print("the element appearing once (XOR of everything):", single)
def single_numbers_two(nums):                                         # two unique numbers among pairs
    xor = 0
    for x in nums: xor ^= x
    low = xor & -xor                                                  # a bit where the two unique numbers differ
    a = b = 0
    for x in nums:
        if x & low: a ^= x
        else: b ^= x
    return sorted((a, b))
print("two unique numbers:", single_numbers_two([1, 2, 1, 3, 2, 5]))
def xor_range(prefix, l, r): return prefix[r + 1] ^ prefix[l]
arr = [random.randint(0, 255) for _ in range(50)]
prefix = [0]
for x in arr: prefix.append(prefix[-1] ^ x)
l, r = 7, 31
direct = 0
for x in arr[l:r + 1]: direct ^= x
print("range XOR via prefix XOR equals direct:", xor_range(prefix, l, r) == direct)
print("Gray code sequence of 3 bits:", [i ^ (i >> 1) for i in range(8)], "(each differs from the previous by one bit)")
