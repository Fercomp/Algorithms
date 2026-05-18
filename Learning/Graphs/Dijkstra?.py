from collections import defaultdict
import heapq
import math

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
    graph[b].append((w, a))

dist = [math.inf] * (n + 1)
parent = [-1] * (n + 1)
dist[1] = 0
heap = [(0, 1)]

while heap:
    d, v = heapq.heappop(heap)
    if d > dist[v]:
        continue

    for w, u in graph[v]:
        if dist[v] + w < dist[u]:
            dist[u] = dist[v] + w
            parent[u] = v
            heapq.heappush(heap, (dist[u], u))

if dist[n] == math.inf:
    print(-1)
else:
    path = []
    current = n
    while current != -1:
        path.append(current)
        current = parent[current]

    path.reverse()
    print(*path)