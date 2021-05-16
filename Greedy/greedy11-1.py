# 기출 문제 - 모험가길드 01
n = input()
data = list(map(int, input().split()))
# 내림차순
data.sort()

count = 0
result = 0

# 1 2 2 2 3 
for item in data:
    count += 1
    if item == count:
        result += 1
        count = 0

print(result)

