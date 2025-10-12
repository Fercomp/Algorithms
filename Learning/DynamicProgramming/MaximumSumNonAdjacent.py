# Rememeber, maximum sum of subsequences
# Obs: this problem don't even make sence because we could only sum all elements
# or if could have negative numbers just discard the negatives
s = [1, 2, 3, 4, 5]

# Basic recursion without dp
def max_sub_sequences(s, i=0, r=[]):
    if len(s) == i:
        return 0
    
    r.append(s[i])
    taken =  max_sub_sequences(s, i + 1, r)
    r.pop()
    not_taken = max_sub_sequences(s, i + 1, r)
    return s[i] + max(taken, not_taken)

# Now the problem states to find all subsequences with no adjacents elements
# This makes more sence, because you cannot take a greedy approach and need to test
# every subsequence
# Time complexity: O(2^n)
# Space complexity: O(n)
def no_adj_max_sub_sequences(s, i=0, r=[]):
    if i >= len(s):
        return 0
    
    r.append(s[i])
    # taken is when i take the current element and sum with the next non adjacent 
    taken = s[i] + no_adj_max_sub_sequences(s, i+2, r)
    r.pop()
    # not taken is when i don't take the current and just consider the problem for the rest
    not_taken = no_adj_max_sub_sequences(s, i+1, r)
    return max(taken, not_taken)

# Optimization using memoization
# Space complexity: O(n)
# Time complexity: O(n)
def no_adj_max_sub_seq(s, i=0, memo={})
    if i >= len(s):
        return 0

    if i in memo:
        return memo[i]
    
    taken = s[i] + no_adj_max_sub_seq(s, i+2, d)
    not_taken = no_adj_max_sub_seq(s, i+1, d)
    memo[i] = max(taken, not_taken)
    return memo[i]

# Optimization using tabulation
# Time complexity: O(n)
# Space complexity: O(n)
def no_adj_max_sub_seq_tab(s):
    n = len(s):
    dp = [0] * n
    dp[0] = s[0]
    dp[1] = max(s[0], s[1])

    for i in range(2, n):
        taken = s[i] + dp[i-2]
        not_taken = dp[i-1]
        dp[i] = max(taken, not_taken)
    return dp[n-1]

# Optimization using current and previus 
# Time complexity: O(n)
# Space complexity: O(1)
def no_adj_max_sub_seq_pp(s):
    n = len(s)
    # As i am going from 2 to n, i need to handle te edge cases when n = 1 or n = 0
    if n == 0:
        return 0
    elif n == 1:
        return s[0]

    previous = s[0]
    current = max(s[0], s[1])

    for i in range(2, n):
        taken = s[i] + previous
        n = max(taken, current)
        previous = current
        current = n

    return current