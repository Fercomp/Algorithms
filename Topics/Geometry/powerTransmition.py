import math

def get_line(x1, y1, x2, y2):
    a = y1 - y2
    b = x2 - x1
    c = a * x1 + b * y1
    gcd = math.gcd(a, math.gcd(b, c))

    if gcd != 0:
        a //= gcd
        b //= gcd
        c //= gcd
        
    if a < 0 or (a == 0 and b < 0):
        a = -a
        b = -b
        c = -c
        
    return (a, b, c)

def has_intersection(a1, b1, c1, a2, b2, c2):
    d = a1 * b2 - a2 * b1
    return d != 0

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

lines = set()
for i in range(0, n):
    for j in range(i+1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        line = get_line(x1, y1, x2, y2)
        lines.add(line)

count = 0
lines = list(lines)
for i in range(0, len(lines)):
    for j in range(i+1, len(lines)):
        a1, b1, c1 = lines[i]
        a2, b2, c2 =lines[j]
        count += 1 if has_intersection(a1, b1, c1, a2, b2, c2) else 0

print(count)