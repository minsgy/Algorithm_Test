# 토마토
from collections import deque
import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

m, n = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, list(input().split()))) for _ in range(n)]
queue = deque()


for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])


# 실행
bfs()

is_State = False
result = -2

for i in matrix:
    for j in i:
        if j == 0:
            is_State = True
            # 익지 않은 토마토
        result = max(result, j)

if is_State == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)
