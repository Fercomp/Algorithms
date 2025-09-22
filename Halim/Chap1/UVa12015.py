import math
t = int(input())
for k in range(1, t+1):
    sites = []
    m = -math.inf

    for _ in range(10):        
        i = input().split()
        s, w = str(i[0]), int(i[1])
        sites.append((s, w))
        m = max(m, w)

    print(f"Case #{k}:")    
    for j in range(10):
        if sites[j][1] == m:
            print(sites[j][0])