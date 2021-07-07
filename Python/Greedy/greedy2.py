# Greedy 실전 2

n, m, k = input().split()
temp = list(map(int, input().split()))
temp.sort(reverse=True)

count = 0
result = 0

for i in range(int(m)):
    if count == int(k):
        result += temp[1]
        count = 0
    else:
        result += temp[0]
        count += 1
    print(result)

print(result)    