# [0][0]
# [1][0], [1][1]
# [2][0], [2][1], [2][2]
# [3][0], [3][1], [3][2], [3][3]


def solution(triangle: list) -> int:
    answer = 0
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        
    
    return max(max(dp))