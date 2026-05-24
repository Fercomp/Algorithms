t = int(input())
for x in range(1, t+1):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    r = int(input())
    soma = 0
    for i in range(r):
        s, d = map(int, input().split())
        soma += graph[s-1][d-1]
        
    print(f"Case #{x}: {soma}")