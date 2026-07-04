n = int(input())
heights = list(map(int, input().split()))
dp = [0] * (n)
dp[0] = 0
dp[1] = abs(heights[0] - heights[1])
for i in range(2, n):
    x = dp[i-1] + abs(heights[i] - heights[i-1])
    y = dp[i-2] + abs(heights[i] - heights[i-2])
    dp[i] = min(x,y)
print(dp[-1])