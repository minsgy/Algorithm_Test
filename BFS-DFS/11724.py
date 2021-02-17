# 연결 요소의 개수 (간 선 구분해야함.)
import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
visited = [False for _ in range(n+1)]
count = 0


def dfs(v):
    visited[v] = True
    for i in range(1, n+1):
        if visited[v] == False and matrix[v][i] == 1:
            dfs(i)


for _ in range(m):
    v, w = map(int, sys.stdin.readline().rstrip().split())
    matrix[v][w] = matrix[w][v] = 1


for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        count += 1

print(count)


# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
