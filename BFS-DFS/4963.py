# 섬의 개수
import sys
from collections import deque
sys.setrecursionlimit(10000)

# 대각선까지
dx = [1, -1, 0, 0, 1, -1, -1, 1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]


while True:
    cnt = 0
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    matrix = [list(map(int, list(sys.stdin.readline().split())))
              for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    def dfs(x, y):
        visited[x][y] = True
        for i in range(8):
            nx, ny = x + dx[i], y+dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if matrix[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)

    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and matrix[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)
