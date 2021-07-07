# 미로 탐색
import sys
from collections import deque

# dx,dy[0] => 오른쪽
# dx,dy[1] => 왼쪽
# dx,dy[2] => 아래
# dx,dy[3] => 위
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, sys.stdin.readline().rstrip().split())

matrix = [list(map(int, list(input()))) for _ in range(n)]  # 정점 개수만큼 matrix 설정
queue = deque()
visited = [[False]*m for i in range(n)]
dist = [[0]*m for _ in range(n)]


queue.append((0, 0))  # 시작점
visited[0][0] = True  # 방문 체크하기
dist[0][0] = 1  # 방문 번째 기록

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False and matrix[nx][ny] == 1:
                queue.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = 1

print(dist[n-1][m-1])
