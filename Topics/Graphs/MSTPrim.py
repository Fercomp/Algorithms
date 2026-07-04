from collections import defaultdict
import heapq

graph = defaultdict(list)
n, m = map(int, input().split())

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

h = []
visited = [0] * n
cost = 0
def process(v):
    visited[v] = 1
    for w, u in graph[v]:
        if not visited[u]:
            heapq.heappush(h, (w, u))

process(0)
while h:
    w, v = heapq.heappop(h)
    if not visited[v]:
        cost += w
        process(v)
        
print(cost)