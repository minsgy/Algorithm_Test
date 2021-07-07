# 안전영역
import sys
sys.setrecursionlimit(10000)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n = int(sys.stdin.readline().rstrip())
count = 0
matrix = [list(map(int, list(sys.stdin.readline().rstrip().split())))
          for _ in range(n)]

visited = [[False] * n for _ in range(n)]
maxValue = 0


def dfs(x, y, h):
    visited[x][y] = True
    global count
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n) and vistied[nx][ny] == False and matrix[nx][ny] > h:
            visited[nx][ny] = True
            dfs(nx, ny, h)


component = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            component += 1
            visited[i][j] = True
            dfs(i, j, k)
