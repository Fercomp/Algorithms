from collections import defaultdict
# Simple code to detect cycles in undirect graphs

def hasCycle(edges):
    graph = defaultdict(list)
    for edge in edges:
        v, u = edge[0], edge[1]
        graph[v].append(u)
        graph[u].append(v)
    
    visited = [0] * (len(graph) + 1)
    
    def dfs(root, parent):
        if visited[root]:
            return True
        
        visited[root] = 1
        for v in graph[root]:
            if v == parent:
                continue
            
            if dfs(v, root):
                return True
            
        return False
    return dfs(1, -1)