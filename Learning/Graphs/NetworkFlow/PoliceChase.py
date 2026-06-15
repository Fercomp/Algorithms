from collections import deque
import math

n, m = map(int, input().split())
network = [[0] * (n + 1) for _ in range(n + 1)]
adj = [[] for _ in range(n + 1)]
edges = []

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    edges.append((u, v))
    network[u][v] += 1
    network[v][u] += 1

def bfs(network):
    parent = [-1] * (n + 1)
    parent[1] = 0
    
    queue = deque([1])
    while queue:
        v = queue.popleft()
        
        for i in adj[v]:
            if parent[i] == -1 and network[v][i] > 0:
                parent[i] = v
                
                if i == n:
                    return parent
                
                queue.append(i)
        
    return None

max_flow = 0
while True:
    parent = bfs(network)
    if parent is None:
        break

    flow = math.inf
    current = n
    while current != 1:
        v = parent[current]
        current_flow = network[v][current]
        flow = min(flow, current_flow)
        current = v
    
    current = n
    while current != 1:
        v = parent[current]
        network[v][current] -= flow
        network[current][v] += flow
        current = v
        
    max_flow += flow

visited = [False] * (n + 1)
def dfs(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v] and network[u][v] > 0:
            dfs(v)

dfs(1)

print(max_flow)
for u, v in edges:
    if visited[u] != visited[v]:
        print(u, v)