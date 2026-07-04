import math
import heapq

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    row = input().split()
    for j in range(1, i):
        val = row[j - 1]

        if val != 'x':
            w = int(val)
            graph[i].append((w, j))
            graph[j].append((w, i))

dist = [math.inf] * (n + 1)
dist[1] = 0
heap = [(0, 1)]

while heap:
    d, v = heapq.heappop(heap)

    if d > dist[v]:
        continue

    for w, u in graph[v]:
        if dist[v] + w < dist[u]:
            dist[u] = dist[v] + w
            heapq.heappush(heap, (dist[u], u))
            
print(max(d for d in dist if d != math.inf))