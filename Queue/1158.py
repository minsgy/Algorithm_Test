n, k = map(int, input().split())
size = [s for s in range(1, n+1)]
result = []

for _ in range(n):
  result.append(size.pop())
