import math
n = int(input())
l = list(map(int, input().split()))

limit = int(1e6)
primes = [True] * (limit + 1)
primes[0] = primes[1] = False

for i in range(2, int(math.sqrt(limit)) + 1):
    if primes[i]:
        for j in range(i * i, limit + 1, i):
            primes[j] = False

for x in l:
    r = int(math.isqrt(x))
    print("YES" if r * r == x and primes[r] else "NO")