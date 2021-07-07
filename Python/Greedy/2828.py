import sys

# 사과 담기 게임
n, m = map(int, input().split())
number = int(sys.stdin.readline().rstrip())

count = 0

for _ in range(number):
    temp = int(sys.stdin.readline().rstrip())
    if temp > m:  # my보다 더 큰 부분에 있을 경우,
        count += abs(m-temp)
        m = temp + m - 1  # 예를들어 1에서 5로 간다하면, 5+1 = 6이 되므로, -1
    elif temp < m:
        count += abs(temp-m)
        m = m-temp+1  # 예를들어, 5에서 3을 간다하면 5-3 = 2가 되므로, +1

print(count)
