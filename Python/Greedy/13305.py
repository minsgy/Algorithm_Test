
n = int(input())

routes = list(map(int, input().split()))
costs = list(map(int, input().split()))

result = routes[0] * costs[0] # 초기값
m = costs[0] # 현재 코스트
dist = 0

for i in range(1, n-1):
    if costs[i] < m: # 이전 코스트 < 현재 코스트 
        result += m*dist
        dist = routes[i]
        m = costs[i]
    else:
        dist+= routes[i]

    if i == n-2:
        result += m*dist
    
print(result)
