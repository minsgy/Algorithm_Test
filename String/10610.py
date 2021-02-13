# 30
import sys

n = sys.stdin.readline().rstrip()
n = list(n)

n.sort(reverse=True)
n_max = int(''.join(n))

if n_max % 30 == 0:
    print(n_max)
else:
    print(-1)
