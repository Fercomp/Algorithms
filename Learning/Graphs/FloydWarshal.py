import math

n, m = map(int, input().split())
graph = [[math.inf] * (n + 1) for _ in range(n + 1)]
pred = [[-1] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0
    pred[i][i] = i

for i in range(m):
    a, b, w = map(int, input().split())
    graph[a][b] = w

for k in range(1, n+1):
    for i in range(1, n+1):
        # Possível otimização 
        if graph[i][k] == math.inf:
            continue

        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            pred[i][j] = pred[k][j]

# Detecção de ciclos
for i in range(1, n + 1):
    if graph[i][i] < 0:
        print("negative cycle")