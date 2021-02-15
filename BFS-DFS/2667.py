# 단지번호 붙히기
# BFS


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


n = int(input())
matrix = [list(map(int, list(input()))) for _ in range(n)]
count = 0
house = []


def dfs(x, y):
    global count
    matrix[x][y] = 0
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if matrix[nx][ny] == 1:
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            count = 0
            dfs(i, j)
            house.append(count)

print(len(house))
house.sort()
for i in house:
    print(i)
