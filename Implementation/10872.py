# 팩토리얼

import sys

n = int(sys.stdin.readline().rstrip())
i = n
result = 1
for i in range(n, 0, -1):
    result *= i

print(result)
