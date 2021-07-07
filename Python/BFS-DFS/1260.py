# DFS와 BFS
import sys
from collections import deque  # 훨씬 효율적인 Queue


# stack에 저장하면서 지워감.
def dfs(v):
    visited[v] = 1  # 방문한 노드 처리
    print(v, end=" ")  # 방문한 노드 출력
    for i in range(1, n+1):
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)

# queue에 저장하며 지워감.


def bfs(v):
    queue = [v]
    visited[v] = 0
    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for i in range(1, n+1):
            if visited[i] == 1 and matrix[v][i] == 1:
                queue.append(i)
                visited[i] = 0


n, m, v = map(int, sys.stdin.readline().rstrip().split())
matrix = [[0]*(n+1) for _ in range(n+1)]  # 정점 개수만큼 matrix 설정
visited = [0 for i in range(n+1)]
for _ in range(n+1):
    # 연결 행렬 만들기.
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    matrix[n1][n2] = 1
    matrix[n2][n1] = 1

dfs(v)
print()
bfs(v)
