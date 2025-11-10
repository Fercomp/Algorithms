def product(x, a, b):
    return (a[0] - x[0]) * (b[1] - x[1]) - (a[1] - x[1]) * (b[0] - x[0])

def convex_hull(vertices):
    if len(vertices) <= 1:
        return vertices

    l = []
    for v in vertices:
        while len(l) >= 2 and product(l[-2], l[-1], v) <= 0:
            l.pop()
        l.append(v)

    u = []
    for v in reversed(vertices):
        while len(u) >= 2 and product(u[-2], u[-1], v) <= 0:
            u.pop()
        u.append(v)

    result = l[:-1] + u[:-1]
    return result

while True:
    n = int(input())
    if n == 0:
        break

    vertices = []
    for _ in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))

    vertices = sorted(list(set(vertices)))
    minimum_points = convex_hull(vertices)
    print(len(minimum_points))
    for x, y in minimum_points:
        print(x, y)