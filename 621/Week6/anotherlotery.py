from math import gcd
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    last_col = []
    total = 0
    for _ in range(n):
        row = list(map(int, input().split()))
        x = row[-1]
        last_col.append(x)
        total += x

    if total == 0:
        for _ in range(n):
            print("0 / 1")
    else:
        for x in last_col:
            g = gcd(x, total)
            print(f"{x // g} / {total // g}")