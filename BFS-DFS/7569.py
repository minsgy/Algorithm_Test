# 토마토
import sys
from collections import deque

n, m, h = map(int, sys.stdin.readline().rstrip().split())

    matrix = [list(map(int, list(sys.stdin.readline().rstrip().split())))
              for _ in range(m*h)]
