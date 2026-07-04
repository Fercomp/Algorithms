import math
def helper(i, j, dims, memo):
    if i == j:
        return 0    
    if (i, j) in memo:
        return memo[(i, j)]
    
    min_mult = math.inf
    for k in range(i, j):
        cost = helper(i, k, dims, memo) + helper(k+1, j, dims, memo) + dims[i] * dims[k+1] * dims[j+1]
        min_mult = min(min_mult, cost)
    
    memo[(i, j)] = min_mult
    return min_mult

n = int(input())
dim = []
for i in range(n):
    r, c = map(int, input().split())
    if i == 0:
        dim.append(r)
    dim.append(c)
memo = {}
print(helper(0, n-1, dim, memo))