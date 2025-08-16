# Naive approach using recursion without memoization or tabulation
def fibonacci1(n):
    if n <= 1:
        return n
    return fibonacci1(n-1) + fibonacci1(n-2)

# Using memoization
def fibonacci2(n, memo=None):
    if memo == None:
        memo = [-1] * (n + 1)
        memo[1] = 1
        memo[0] = 0
    
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fibonacci2(n-1, memo) + fibonacci2(n-2, memo)
    return memo[n]
    
print(fibonacci2(2))
print(fibonacci2(3))
print(fibonacci2(4))
print(fibonacci2(5))
print(fibonacci2(6))
print(fibonacci2(7))
print(fibonacci2(52))
