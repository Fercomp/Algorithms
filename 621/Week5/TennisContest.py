def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)  

def comb(n, k):
    return fac(n) // (fac(k) * fac(n - k))

import math
t = int(input())
for _ in range(t):
    n = int(input())
    p = float(input())
    total = 0.0
    for i in range(n, 2 * n):
        ways = math.comb(i - 1, n - 1)
        prob = (p ** n) * ((1 - p) ** (i - n))
        total += ways * prob
    print(f"{total:.2f}")