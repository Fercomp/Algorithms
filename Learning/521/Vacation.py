import math
n = int(input())
days = []
for _ in range(n):
    day = list(map(int, input().split()))
    days.append(day)

def best_sum(days):
    dp = [[0] * 3 for _ in range(n)]
    dp[0][0], dp[0][1], dp[0][2] = days[0][0], days[0][1], days[0][2]

    
    for i in range(1, n):
        for j in range(3):
            best = -math.inf
            for k in range(3):
                if j != k:
                    best = max(best, days[i][j] + dp[i-1][k])
            dp[i][j] = best
    return max(dp[-1])

print(best_sum(days))