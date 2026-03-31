import sys
import math

def equation(x, p, q, r, s, t, u):
    return p * math.exp(-x) + q * math.sin(x) +  r * math.cos(x) +  s * math.tan(x) +  t * x ** 2 + u

for input in sys.stdin:
    p, q, r, s, t, u = map(int, input.split())
    f0 = equation(0.0, p, q, r, s, t, u)
    f1 = equation(1.0, p, q, r, s, t, u)
    
    if f0 * f1 > 0:
        print("No solution")
        continue
    
    l = 0.0
    h = 1.0
    for _ in range(100):
        mid = (l + h) / 2.0
        if equation(mid, p, q, r, s, t, u) > 0:
            l = mid
        else:
            h = mid 
    print(f"{l:.4f}")