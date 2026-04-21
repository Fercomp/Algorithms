points = [[1,2,5],
          [3,1,1],
          [3,3,3]]

# Time: O(2^n)
# Space: O(n)
def ninjaTraining(points):
    def helper(points, index, previous, memo):
        if (index, previous) in memo:
            return memo[(index, previous)]
        
        if index < 0:
            return 0
        better = 0
        for i in range(3):
            if i != previous:
                better = max(better, points[i][index] + helper(points, index - 1, i, memo))
        
        memo[(index, previous)] = better
        return better
    
    memo = {}
    return helper(points, len(points)-1, 4, memo)

# Time: O(n)
# Space: O(3n)
def dpNinjaTraining(points):
    dp = [[0] * 3 for _ in range(len(points[0]))]
    dp[0][0], dp[1][0], dp[2][0] = points[0][0], points[1][0], points[2][0]
    
    for i in range(1, len(dp[0])):
        for j in range(3):
            better = 0
            for k in range(3):
                if k != j:
                    better = max(better, points[j][i] + dp[k][i-1])
            dp[j][i] = better
            
    return max(dp[0][-1], dp[1][-1], dp[2][-1])

print(ninjaTraining(points))
print(dpNinjaTraining(points))