# UVa10048
import math
count = 1
while True:
    c, s, q = map(int, input().split())
    if c == 0 and s == 0 and q == 0:
        break
    
    graph = [[math.inf] * (c + 1) for _ in range(c + 1)]
    
    for _ in range(s):
        c1, c2, d = map(int, input().split())
        graph[c1][c2] = d
        graph[c2][c1] = d
    
    for i in range(c+1):
        graph[i][i] = 0
        

    for k in range(0, c+1):
        for i in range(0, c+1):
            for j in range(0, c+1):
                graph[i][j] = min(graph[i][j], max(graph[i][k], graph[k][j]))
                
    if count > 1:
        print()
    
    print(f"Case #{count}")
    for _ in range(q):
        u, v = map(int, input().split())
        if graph[u][v] == math.inf:
            print("no path")
        else:
            print(graph[u][v])
        
    count += 1