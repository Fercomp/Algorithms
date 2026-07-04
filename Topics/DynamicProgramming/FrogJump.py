energy = [10, 20, 30, 50]

# Basic solution using plain recursion (inefficient).
# Time: O(2^n), Space: O(n) due to recursion stack
def min_energy(energy, i):
    if i == 0:
        return 0
    if i == 1:
        return abs(energy[1] - energy[0])

    p = abs(energy[i] - energy[i-1]) + min_energy(energy, i-1)
    pp = abs(energy[i] - energy[i-2]) + min_energy(energy, i-2)
    return min(p, pp)

# Recursion with memoization (top-down DP).
# First check if result is already stored, otherwise compute and cache it.
# Time: O(n), Space: O(n)
def min_energy_memo(energy, i, r=None):
    if r is None:
        r = {}

    if i == 0:
        r[i] = 0
        return r[i]
    if i == 1:
        r[i] = abs(energy[1] - energy[0])
        return r[i]

    if i in r:
        return r[i]

    p = abs(energy[i] - energy[i-1]) + min_energy_memo(energy, i-1, r)
    pp = abs(energy[i] - energy[i-2]) + min_energy_memo(energy, i-2, r)
    r[i] = min(p, pp)
    return r[i]

# Iterative DP (tabulation).
# Build the solution bottom-up storing all subproblems.
# Time: O(n), Space: O(n)
def min_energy_tab(energy):
    n = len(energy)
    dp = [-1] * n
    dp[0] = 0
    if n > 1:
        dp[1] = abs(energy[1] - energy[0])

    for i in range(2, n):
        p = abs(energy[i] - energy[i-1]) + dp[i-1]
        pp = abs(energy[i] - energy[i-2]) + dp[i-2]
        dp[i] = min(p, pp)

    return dp[n-1]

# Iterative DP optimized for space.
# Keep only the last two states instead of the full dp array.
# Time: O(n), Space: O(1)
def min_energy_tab2(energy):
    n = len(energy)
    if n == 1:
        return 0
    pp = 0
    p = abs(energy[1] - energy[0])

    for i in range(2, n):
        a = min(abs(energy[i] - energy[i-1]) + p,
                abs(energy[i] - energy[i-2]) + pp)
        pp, p = p, a
    return p

print(min_energy(energy, len(energy) - 1))
print(min_energy_memo(energy, len(energy) - 1))
print(min_energy_tab(energy))
print(min_energy_tab2(energy))