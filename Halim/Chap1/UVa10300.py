t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        count += a * c
    print(count)