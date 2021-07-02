dx = [2, 1, -2, -1, 2, 1, -2, -1]
dy = [1, 2, 1, 2, -1, -2, -1, -2]
count = 0

# def bfs(v, x, y):

def solution(n):
  for _ in range(n):
    i = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    visited = [[False]*n for _ in range(n)]
    maps = [[0]*n for _ in range(n)]

n = int(input())
solution(n)