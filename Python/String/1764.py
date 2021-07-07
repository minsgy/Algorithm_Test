# 듣보잡
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())

N_list = set([sys.stdin.readline().strip() for i in range(N)])
M_list = set([sys.stdin.readline().strip() for i in range(M)])

n_m = sorted(list(N_list & M_list))
print(len(n_m))

for i in n_m:
    print(i)
