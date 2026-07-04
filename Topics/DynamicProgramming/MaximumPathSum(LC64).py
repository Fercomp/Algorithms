import math

# Naive recursion
# Time: O(2^(m+n))
# Space: O(m+n)
def min_path_sum_naive(grid):
    
    def helper(grid, i, j):
        if i == 0 and j == 0:
            return grid[0][0]
        elif i < 0 or j < 0:
            return math.inf
        
        return grid[i][j] + min(helper(grid, i-1, j), helper(grid, i, j-1))

    return helper(grid, len(grid)-1, len(grid[0]) - 1)

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(min_path_sum_naive(grid))
    
# Tabulation approach
# Time: O(n * m)
# Space: O(n * m)
def min_path_sum_tab(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[0][0] = grid[0][0]
                continue

            up = dp[i-1][j] if i-1 >= 0 else math.inf
            left = dp[i][j-1] if j-1 >= 0 else math.inf
            dp[i][j] = grid[i][j] + min(up, left)

    return dp[n-1][m-1]