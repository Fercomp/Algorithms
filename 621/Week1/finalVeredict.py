t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    if sum(l) / n == x:
        print("YES")
    else:
        print("NO")