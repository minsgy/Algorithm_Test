# 결혼식
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
# 연결 간선을 나타내는 인접 리스트를 생각해보자..
# 행렬 배열로 만드는건 시간이 비효율적으로 증가함.
adj = [[] for _ in range(n+1)]

visited = [False for _ in range(n+1)]
cnt = 0
level = 0  # 시작부터 단계로나누어 친구의 친구까지 판별한다.


for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append(b)  # 연결 값만 저장함.
    adj[b].append(a)


def bfs(v):
    global level, cnt
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        level += 1
        for _ in range(len(queue)):
            v = queue.popleft()
            for i in adj[v]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    cnt += 1
        if level == 2:
            break


bfs(1)  # 상근이 학번은 1로 시작해서 2단계 내려가도록 탐색
print(cnt)
