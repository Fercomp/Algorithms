# https://cses.fi/problemset/task/1666
n, m = map(int, input().split())
graph = { i: [] for i in range(1, n+1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(root, visited):
    visited[root] = 1
    stack = [root]
    
    while stack:
        v = stack.pop()
        
        for u in graph[v]:
            if not visited[u]:
                visited[u] = 1
                stack.append(u)
            
visited = [0] * (n+1)
component = 0
representatives = []

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, visited)
        representatives.append(i)

print(len(representatives) - 1)
for i in range(1, len(representatives)):
    print(f"{representatives[i-1]} {representatives[i]}")