from collections import deque
import math

flow_threshold = 1 << 30
n, m = map(int, input().split())
network = [[0] * (n + 1) for _ in range(n + 1)]
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    
    if network[u][v] == 0 and network[v][u] == 0:
        adj[u].append(v)
        adj[v].append(u)
    
    network[u][v] += w

def bfs(network):
    parent = [-1] * (n + 1)
    parent[1] = 1
    
    queue = deque([1])
    while queue:
        v = queue.popleft()
        
        for i in adj[v]:
            if parent[i] == -1 and network[v][i] >= flow_threshold:
                parent[i] = v
                
                if i == n:
                    return parent
                
                queue.append(i)
        
    return None


max_flow = 0

while flow_threshold > 0:
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
    
    flow_threshold //= 2

print(max_flow)