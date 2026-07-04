# leetcode.com/problems/unique-paths
m = 3
n = 7

dp = [[0] * n for _ in range(m)]
dp[0][0] = 1

for i in range(m):
    for j in range(n):
        left = 0
        up = 0
        if j - 1 >= 0:
            left = dp[i][j-1]
        if i -1 >= 0:
            up = dp[i-1][j]
        
        dp[i][j] += left + up
        
print(dp[-1][-1])