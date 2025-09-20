while True:
    t = int(input())
    if t == 0:
        break
    x_c, y_c = map(int, input().split())
    for _ in range(t):
        x, y = map(int, input().split())
        if x > x_c and y > y_c:
            print("NE")
        elif x < x_c and y > y_c:
            print("NO")
        elif x < x_c and y < y_c:
            print("SO")
        elif x > x_c and y < y_c:
            print("SE")
        else:
            print("divisa")