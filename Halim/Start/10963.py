t = int(input())
while t > 0:
    t -= 1
    b = input()
    r = int(input())
    y1, y2 = map(int, input().split())
    d = y1 - y2
    valid = True
    for _ in range(1, r):
        x1, x2 = map(int, input().split())
        d_a = x1 - x2
        if d != d_a:
            valid = False
    if not valid:
        print("no")
    else:
        print("yes")
    if t > 1:
        print('')