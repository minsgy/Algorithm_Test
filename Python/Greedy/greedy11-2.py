# 기출 문제 - 곱하기 혹은 더하기
s = list(input())
s.sort(reverse=True)

result = 1
for item in s:
    if item == '0':
        continue
    elif item == '1':
        result += int(item)
    else:
        result *= int(item) 

print(result)       
