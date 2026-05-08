import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = [False] * (n + 1)
def dfs(u, order):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, order)
    order.append(u)

order = []
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, order)

order.reverse()
routes = [0] * (n + 1)
routes[1] = 1
for u in order:
    for v in graph[u]:
        routes[v] = (routes[v] + routes[u]) % (10**9 + 7)

print(routes[n])