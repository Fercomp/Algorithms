# https://cses.fi/problemset/task/1195

from collections import defaultdict
import math
import heapq

n, m = map(int, input().split())
graph = defaultdict(list)

for i in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))

dist = [math.inf] * (n + 1)
parents = [-1 ] * (n + 1)
dist[1] = 0
heap = [(0, 1)]
heapq.heapify(heap)

while heap:
    d, v = heapq.heappop(heap)
    
    if d > dist[v]:
        continue
    
    for w, u in graph[v]:
        if dist[v] + w < dist[u]:
            dist[u] = dist[v] + w
            parents[u] = v
            heapq.heappush(heap, (dist[u], u))

current = n
max_edge = 0
while current != -1:
    parent = parents[current]
    max_edge = max(max_edge, dist[current] - dist[parent])
    current = parent

print(dist[n] - (max_edge // 2))