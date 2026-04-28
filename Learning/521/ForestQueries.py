n, q = map(int, input().split())
mapa = [list(input()) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        up = dp[i-1][j] if i > 0 else 0
        left = dp[i][j-1] if j > 0 else 0
        dag = dp[i-1][j-1] if i > 0 and j > 0 else 0
        val = 1 if mapa[i][j] == "*" else 0
        dp[i][j] = up + left - dag + val

for _ in range(q):
    y1, x1, y2, x2 = map(int, input().split())
    y1, x1, y2, x2 = y1-1, x1-1, y2-1, x2-1
    total = dp[y2][x2]
    if y1 > 0:
        total -= dp[y1-1][x2]
    if x1 > 0:
        total -= dp[y2][x1-1]
    if y1 > 0 and x1 > 0:
        total += dp[y1-1][x1-1]
    print(total)