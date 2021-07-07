# 문자열 재정렬
s = list(input())
sum_int = 0
result = []
s.sort()
for item in s:
  temp = item.isdigit()
  if temp: 
    sum_int += int(item)
  else:
    result.append(item)
result.append(str(sum_int))
result = "".join(result)
print(result)