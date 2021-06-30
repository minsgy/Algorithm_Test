# 백준 - 1, 2, 3으로 합하기
def solution(n):
  input_list = []

  for _ in range(n):
    input_list.append(int(input()))
  
  # 예외처리 ( n > 3 )
  dp = [1, 2, 4]
  
  for i in range(3, max(input_list)):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

  for i in input_list:
    print(dp[i-1])
    
n = int(input())
solution(n)