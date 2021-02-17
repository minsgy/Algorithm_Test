# 바이러스
import sys

n = int(sys.stdin.readline().rstrip())
router = int(sys.stdin.readline().rstrip())

matrix = [[0]*(n+1) for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = -1  # 1번 컴퓨터는 제외다.

for _ in range(router):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    matrix[x][y] = matrix[y][x] = 1


def dfs(v):
    global cnt
    visited[v] = True
    cnt += 1
    for i in range(1, n+1):
        if visited[i] == False and matrix[v][i] == 1:
            dfs(i)


dfs(1)

print(cnt)
