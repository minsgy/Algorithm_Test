# 럭키 스트레이트

n = list(map(int, input()))
mid = len(n) // 2
# print(mid)
if sum(n[0:mid]) == sum(n[mid:len(n)]):
  print("LUCKY")
else:
  print("READY")