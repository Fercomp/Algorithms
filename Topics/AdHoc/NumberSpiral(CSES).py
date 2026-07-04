t = int(input())
for _ in range(t):
    y, x = map(int, input().split())
    ma = max(x, y)
    mi = min(x, y)
    ii = ma ** 2 - ma + 1
    diff = abs(ma - mi)
    if y % 2 == 0:
        print(ii + diff)
    else:
        print(ii - diff)
