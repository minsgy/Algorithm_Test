# 왕실의 나이트

point = input()

step_value = [
  [-2, -1],
  [-1, -2],
  [1, -2],
  [2, -1],
  [2, 1],
  [1, 2],
  [-1, 2],
  [-2, 1]
]

row = int(point[1])
cols = int(ord(point[0])) - int(ord('a')) + 1

result = 0
for x, y in step_value:
  next_x = x + row
  next_y = y + cols
  if next_x >= 1 and next_x <= 8 and next_y >= 1 and next_y <= 8:
    result += 1


print(result)