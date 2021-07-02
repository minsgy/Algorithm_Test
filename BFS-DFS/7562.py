from collections import deque
dx = [2, 1, -2, -1, 2, 1, -2, -1]
dy = [1, 2, 1, 2, -1, -2, -1, -2]

def bfs(maps, start_x, start_y, end_x, end_y):
  queue = deque()
  queue.append([start_x, start_y])
  maps[start_x][start_y] = 1
  print(end_x, end_y)
  while queue:
    x, y = queue.popleft()
    if x == end_x and y == end_y:
      print(maps[x][y])
      break
    for i in range(8):
      nx = dx[i] + x
      ny = dx[i] + y
      if 0 <= nx < len(maps) and 0 <= ny < len(maps) and maps[nx][ny] == 0:
        # print(queue)
        queue.append([nx, ny])
        maps[nx][ny] = maps[x][y] + 1

def solution(n):
  answer = []
  for _ in range(n):
    i = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    maps = [[0] * i for _ in range(i)]    
    bfs(maps, start_x, start_y, end_x, end_y)


n = int(input())
solution(n)