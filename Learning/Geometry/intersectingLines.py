
n = int(input())

print("INTERSECTING LINES OUTPUT")
for _ in range(n):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    
    a1 = y1 - y2
    b1 = x2 - x1
    c1 = a1 * x1 + b1 * y1

    a2 = y3 - y4
    b2 = x4 - x3
    c2 = a2 * x3 + b2 * y3

    d = a1 * b2 - a2 * b1
    x = c1 * b2 - c2 * b1
    y = a1 * c2 - a2 * c1

    if d != 0:
        x = x / d
        y = y / d
        print(f"POINT {x:.2f} {y:.2f}")
    else:
        if x == 0 and y == 0:
            print("LINE")
        else:
            print("NONE")

print("END OF OUTPUT")