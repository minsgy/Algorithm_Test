# 파이프 옮기기 1
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

matrix = [list(map(int, list(sys.stdin.readline().rstrip().split())))
          for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dist = [[0]*n for _ in range(n)]


def dfs(v):
    visited[True]
