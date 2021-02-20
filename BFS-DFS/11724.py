import sys
# 연결 요소 개수
N, M = map(int, sys.stdin.readline().split())

adj = [[]for i in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
visit_list = [0]*(N+1)


def bfs(v):
    queue = [v]
    while queue:
        v = queue.pop(0)
        for i in adj[v]:
            if visit_list[i] == 0:
                queue.append(i)
                visit_list[i] = 1


answer = 0
for i in range(1, N+1):
    if visit_list[i] == 0:
        bfs(i)
        answer += 1

sys.stdout.write(str(answer))
