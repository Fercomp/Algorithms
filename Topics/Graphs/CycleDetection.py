from collections import defaultdict
from collections import deque

# Cycle detection in bidirectional graph using bfs
def cycle_detection_bidirectional_bfs(edges, s):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    n = max(max(u, v) for u, v in edges)
    visited = [0] * (n + 1)
    visited[s] = 1
    q = deque([(s, -1)])
    
    while q:
        vertex, parent = q.popleft()
        for u in graph[vertex]:
            if u == parent:
                continue
            
            elif visited[u]:
                return True
            
            else:
                q.append([u, vertex])
                visited[u] = 1
            
    return False

# Cycle detection in bidirectional graph using dfs
def cycle_detection_bidirectional_dfs(edges, s):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
        
    n = max(max(u, v) for u, v in edges)
    visited = [0] * (n + 1)
    
    def dfs(root, parent):
        visited[root] = 1
        for v in graph[root]:
            
            if v == parent:
                continue
            
            if visited[v]:
                return True
            
            if dfs(v, root):
                return True
            
        return False

    return dfs(s, -1)

# Cycle detection in unidirectional graph using dfs
def cycle_detection_unidirectional_bfs(edges, s):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
    
    n = max(max(u, v) for u, v in edges)
    visited = [0] * (n + 1)
    def dfs(root):
        visited[root] = 1
        
        for v in graph[root]:
            if visited[v] == 1:
                return True
            if visited[v] == 0 and dfs(v):
                return True

        visited[root] = 2
        return False
    
    return dfs(s)