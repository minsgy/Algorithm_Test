# BOJ - 동전 1
def solution(n, k):
  dp = [0] * (k+1)
  coin = []
  for _ in range(n):
    coin.append(int(input()))

  for c in coin:
    for i in range(1, k+1):
      if i == c: # 지정된 동전 사용 시의 예외처리해야함.
        dp[i] += 1
      elif i > c: # i가 더 커야 계산되기 때문에..
        dp[i] += dp[i-c]


  print(dp[k])

n, k = input().split()
solution(int(n), int(k))