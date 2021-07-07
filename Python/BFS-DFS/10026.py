import sys


def bfs(color, i, j):
    q = [(i, j)]

    while len(q) != 0:
        pos = q.pop(0)  # x, y
        x = pos[0]  # x
        y = pos[1]  # y

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < n and matrix[nx][ny] in color and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
matrix = [list(map(lambda x: list(x), sys.stdin.readline().split()))[0]
          for _ in range(n)]

visited = [[False] * n for _ in range(n)]
nblind = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(list(matrix[i][j]), i, j)
            nblind += 1

visited = [[False] * n for _ in range(n)]
blind = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            if matrix[i][j] == 'R' or matrix[i][j] == 'G':
                bfs(['R', 'G'], i, j)
            else:
                bfs(['B'], i, j)
            blind += 1

print(nblind, blind)
