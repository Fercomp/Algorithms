import math

while True:
    try:
        line = input().split()
        if not line:
            break
    except EOFError:
        break
    n, time = map(int, line)
    x = 0.0
    y = 0.0
    d = []

    for _ in range(n):
        r, t = map(float, input().split())
        a = (2.0 * math.pi) * time / t
        x += r * math.cos(a)
        y += r * math.sin(a)
        
        dist = math.sqrt(x ** 2 + y **2)
        d.append(f"{dist:.4f}")

    print(" ".join(d))