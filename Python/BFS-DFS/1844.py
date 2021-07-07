# 프로그래머스 - 게임 맵 최단 거리
from collections import deque
def solution(maps: list) -> int:
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    queue = deque()
    queue.append([0, 0, 1])

    while queue:
        y, x, count = queue.popleft()
        maps[y][x] = 0        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if x == len(maps[0]) - 1 and y == len(maps) - 1:
                return count
            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and maps[ny][nx] == 1:
                maps[ny][nx] = 0
                queue.append((ny, nx, count+1))

    return -1