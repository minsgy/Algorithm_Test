# BOJ - 1로 만들기
# dp[i] = min(dp[i-1]+1, dp[i//2]+1, dp[i//3]+1)
def solution(x):

  dp = [0] * (x+1)

  for i in range(2, x+1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
      dp[i] = min(dp[i], dp[i // 2] + 1)
      
    if i % 3 == 0:
      dp[i] = min(dp[i], dp[i // 3] + 1)
    
  print(dp[x])



x = int(input())
solution(x)