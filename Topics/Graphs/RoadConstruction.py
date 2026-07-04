from collections import defaultdict
import heapq
import math

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    graph = defaultdict(list)
    for _ in range(m):
        u, v, d, c = map(int, input().split())
        graph[u].append((d, v, c))
        graph[v].append((d, u, c))
    
    h = [(0, 1)]
    dist = [math.inf] * (n + 1)
    dist[1] = 0
    
    while h:
        d, v = heapq.heappop(h)

        if d > dist[v]:
            continue

        for w, u, _ in graph[v]:
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                heapq.heappush(h, (dist[u], u))
    
    min_cost = [math.inf] * (n + 1)
    for u in range(1, n + 1):
        for d, v, c in graph[u]:
            if dist[u] + d == dist[v]:
                min_cost[v] = min(min_cost[v], c)
                
    print(sum(min_cost[2:]))