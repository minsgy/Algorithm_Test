# 그룹 단어 체커

n = int(input())
count = 0
for i in range(n):
  temp_list = []
  state = True
  temp = list(input())
  for i in range(len(temp)):
    if temp[i] not in temp_list:
      temp_list.append(temp[i])
    elif temp[i-1] == temp[i]:
      continue
    else:
      state = False
      break
  if state:
    count+=1

print(count)