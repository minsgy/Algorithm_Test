# Greedy 실전 3 - 숫자카드게임

n, m = input().split()
result = [] 
for i in range(int(n)):
    data = list(map(int, input().split()))
    result.append(min(data))

print(max(result))