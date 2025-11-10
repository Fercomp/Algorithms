while True:
    n = int(input().strip())
    if n == 0:
        break

    vertices = []
    for _ in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))

    x, y = map(int, input().split())
    is_in = False
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]

        if y1 == y2:
            continue

        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        if y1 <= y < y2:
            
            inter_x = x1
            if inter_x > x:
                is_in = not is_in

    if is_in:
        print('T')
    else:
        print('F')