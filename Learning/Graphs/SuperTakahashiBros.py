# https://vjudge.net/contest/816350#problem/I
import heapq
from collections import defaultdict
import math

n = int(input())
graph = defaultdict(list)
for i in range(1, n):
    a, b, w = map(int, input().split())
    graph[i].append((a, i+1))
    graph[i].append((b, w))

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

print(dist[n])