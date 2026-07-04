# Recursive climbing the stair
# Time: O(2^n)
# Space: O(n)
def climbing_the_stairs_r(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return climbing_the_stairs_r(n-1) + climbing_the_stairs_r(n-2)

# Memoization climbing the stair
# Time: O(n)
# Space: O(n)
def climbing_the_stairs_r(n, memo={}):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    if n in memo:
        return memo[n]
    memo[n] = climbing_the_stairs_r(n-1) + climbing_the_stairs_r(n-2)
    return memo[n]

# Tabulation
# Time: O(n)
# Space: O(n)
def climbing_the_stairs(n):
    dp = [-1] * (n+1)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# The same principle apply to the climbing with 3 steps
def climbing_the_stairs_with_tree_steps(n):
    dp = [-1] * (n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

# Now we have different costs in every step, and we want to get the minimum
def minimum_cost_to_reach_the_top(n, c):
    dp = [-1] * (n+1)
    dp[0] = c[0]
    dp[1] = c[1]
    for i in range(2, n+1):
        dp[i] = min(dp[i-1] + c[i], dp[i-2] + c[i])
    return dp[n]