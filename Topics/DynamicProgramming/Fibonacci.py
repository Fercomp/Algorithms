# Naive approach using recursion without memoization or tabulation
# T(n) = O(n^2)
# If a binary tree have height n, it will have 2^n nodes, so n^2 operations 
def fibonacci1(n):
    if n <= 1:
        return n
    return fibonacci1(n-1) + fibonacci1(n-2)

# Using memoization
# Time: O(n)
# Space: O(n)
def fibonacci2(n, memo=None):
    if memo == None:
        memo = [-1] * (n + 1)
        memo[1] = 1
        memo[0] = 0
    
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fibonacci2(n-1, memo) + fibonacci2(n-2, memo)
    return memo[n]

# Using tabulation
# Time: O(n)
# Space: O(n)
def fibonacci3(n):
    dp = [-1] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Using tabulation with optimized space
# Time: O(n)
# Space: O(1)
def fibonacci4(n):
    pp = 0
    p = 1
    c = 1
    for _ in range(2, n+1):
        c = p + pp
        pp = p
        p = c
    return c