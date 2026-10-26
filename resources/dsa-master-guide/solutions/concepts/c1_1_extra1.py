# Template 1: first line n, second line n numbers
n = int(input())
nums = list(map(int, input().split()))

# Template 2: several test cases
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum(arr))            # one answer per line

# Template 3: read everything fast (large inputs)
import sys
data = sys.stdin.read().split()
n = int(data[0])
nums = list(map(int, data[1:1 + n]))

# Output formats
print(*nums)                   # 1 2 3  (space separated)
print("\n".join(map(str, nums)))   # one per line
print(f"{3.14159:.2f}")        # 3.14 -> fixed decimals
