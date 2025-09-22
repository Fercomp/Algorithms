import sys
import math

for line in sys.stdin:
    n, b, h, w = map(int, line.strip().split())
    best = math.inf

    for _ in range(h):
        price = int(input())
        l = list(map(int, input().split()))
        if max(l) >= n: 
            best = min(best, price * n)
    
    if best != math.inf and best <= b:
        print(best)
    else:
        print("stay home")
