a, b, c = map(int, input().split())
wanted_balls = (b * c)
if a <= wanted_balls:
    print(a / b)
else:
    print(c)