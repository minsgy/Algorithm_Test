import sys
# 팬덤이 넘쳐흘러
time = 0
n = int(sys.stdin.readline().rstrip())
fan_list = []
for _ in range(n):
    fan_list.append(list(map(int, sys.stdin.readline().split())))

first = sorted(fan_list, key=lambda x: x[0])
last = sorted(fan_list, key=lambda x: x[1])

time = first[-1][0] - last[0][1]

if time > 0:
    print(time)
else:
    print(0)
