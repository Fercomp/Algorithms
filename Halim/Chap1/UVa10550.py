def grades_between(a, b):
    if a < b:
        return b - a
    else:
        return (39 - b + 1) + a

while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    g = int(360 / 40)
    count = 360 * 2
    count += grades_between(a, b) * g
    count += 360
    count += grades_between(b, c) * g
    count += grades_between(c, d) * g
    print(count)