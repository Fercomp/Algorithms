from collections import defaultdict

def findRedundantConnection(edges):
    graph = defaultdict(list)    
    for edge in edges:
        v, u = edge[0], edge[1]
        graph[v].append(u)
        graph[u].append(v)
    
    visited = [0] * (len(graph) + 1)
    redundand_edges = set()
    
    def dfs(root, parent):
        if visited[root]:
            redundand_edges.add((parent, root))
            return True
        
        visited[root] = 1
        for v in graph[root]:
            if v == parent:
                continue
            
            if dfs(v, root):
                redundand_edges.add((parent, root))
                return True
            
        return False
    
    dfs(1, -1)
    return max(redundand_edges, key=lambda x: x[0])