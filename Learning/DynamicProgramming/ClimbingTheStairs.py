# It's the same thing but we are counting how many ways 
# So to reach the n stair we can came from the previus n-1 stair or n-2 stair
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