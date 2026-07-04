t = int(input())
for _ in range(t):
    n, c, k = map(int, input().split())
    monsters = list(map(int, input().split()))
    monsters.sort()
    for i in range(n):
        if c < monsters[i]:
            break
        
        difference = c - monsters[i]
        x = min(k, difference)
        c += monsters[i] + x
        k = max(k-difference, 0)
    print(c)