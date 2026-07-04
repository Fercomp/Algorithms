import math
energy = [15, 4, 1, 14, 15]
k = 3

# Recursive approach without optimization 
# Time O(nˆk), Space O(n)
def min_energy(energy, i, k):
    if i <= 0:
        return 0

    min_e = math.inf
    for j in range(1, k+1):
        if i-j >= 0:
            p = min_energy(energy, i-j, k) + abs(energy[i] - energy[i-j])
            min_e = min(min_e, p)
    
    return min_e

# Using memoization
# Time O(n * k), Space O(n)
# every i we need to look at the k elements before so O(n * k)
def min_energy_memo(energy, i, k, m=None):
    if m == None:
        m = dict()

    if i <= 0:
        return 0
    
    if i in m:
        return m[i]
    
    min_e = math.inf
    for j in range(1, k+1):
        if i - j >= 0:
            p = min_energy_memo(energy, i-j, k, m) + abs(energy[i] - energy[i-j])
            min_e = min(p, min_e)
    
    m[i] = min_e
    return m[i]

# Tabulation time O(n * k), Space O(n)
def min_energy_tab(energy, k):
    n = len(energy)
    dp = [-1] * n
    dp[0] = 0

    # Attention: We need to start after the initial case, because if we do the base case again starting
    # from i = 0, we will go to line 53 straighfoward and change dp[0] to inf, and everything will be 
    # wrong
    for i in range(1, n):
        min_e = math.inf
        for j in range(1, k+1):
            if i - j >= 0:
                p = dp[i - j] + abs(energy[i] - energy[i-j])
                min_e = min(min_e, p)
        dp[i] = min_e
    
    return dp[n-1]

print(min_energy(energy, len(energy) - 1, k))
print(min_energy_memo(energy, len(energy) - 1, k))
print(min_energy_tab(energy, k))