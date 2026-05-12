from collections import defaultdict

def has_topological_sort(edges, s):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        
    n = max([max(u, v) for u, v in edges])
    visited = [0] * (n + 1)
    
    def dfs(root):
        visited[root] = 1
        
        for v in graph[root]:
            if visited[v] == 1:
                return False
            
            if visited[v] == 0 and not dfs(v):
                return False
        
        visited[root] = 2
        return True

    return dfs(s)

def topological_sort(edges, s):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        
    n = max([max(u, v) for u, v in edges])
    visited = [0] * (n + 1)
    
    result = []
    def dfs(root):
        visited[root] = 1
        for v in graph[root]:
            if visited[v] == 1:
                return False
            
            if visited[v] == 0 and not dfs(v):
                return False
        
        visited[root] = 2
        result.append(root)
        return True

    if not dfs(s):
        return []
    
    return result[::-1]