obstacleGrid = [[0,0,0],
                [0,1,0],
                [0,0,0]]

dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]

dp[0][0] = 1
for i in range(len(dp)):
    for j in range(len(dp[0])):
        left = 0
        up = 0
        if j - 1 >= 0 and obstacleGrid[i][j-1] == 0:
            left = dp[i][j-1]
        if i - 1 >= 0 and obstacleGrid[i-1][j] == 0:
            up = dp[i-1][j]
        dp[i][j] += left + up

print(dp[-1][-1])