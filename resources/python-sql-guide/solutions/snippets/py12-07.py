print(-7 // 2, -7 % 2, int(-7 / 2), round(0.5), round(1.5), round(2.5))
print("exact big integers:", 2 ** 100, "| float limit:", 1e308 * 10, "| inf comparisons:", float("inf") > 10 ** 100)
to_int32 = lambda x: (x + 2**31) % 2**32 - 2**31
print("simulated int32 overflow:", to_int32(2**31), to_int32(2**31 - 1 + 5))
print("float equality pitfalls:", 0.1 + 0.2 == 0.3, abs(0.1 + 0.2 - 0.3) < 1e-9)
