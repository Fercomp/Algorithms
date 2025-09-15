import sys

# Primeira ideia 
# for line in sys.stdin:
#     n, k = map(int, line.split())
#     soma = 0
#     for i in range(k, n+1):
#         soma += n - i + 1
#     print(soma)

# Segunda ideia 

import math
for line in sys.stdin:
    n, k = map(int, line.split())
    dp = [0] * (n + 1)
    dp[k] = 1
    for i in range(k+1, n+1):
        dp[i] = dp[i-1] + 2
    print(dp[n])
