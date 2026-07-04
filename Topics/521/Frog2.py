import math
n, k = map(int, input().split())
heights = list(map(int, input().split()))
dp = [0] * (n)
dp[0] = 0
for i in range(1, n):
    min_value = math.inf
    for j in range(1, k+1):
        if i - j >= 0:
            x = dp[i-j] + abs(heights[i] - heights[i-j])
            min_value = min(min_value, x)
    dp[i] = min_value
print(dp[-1])