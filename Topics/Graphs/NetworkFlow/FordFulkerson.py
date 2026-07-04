import math
n, m = map(int, input().split())
network = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    network[u][v] += w

def dfs(v, flow, visited, network):
    if v == n:
        return flow

    visited[v] = True

    for i in range(1, n + 1):
        if not visited[i] and network[v][i] > 0:

            min_flow = dfs(i, min(flow, network[v][i]), visited, network)

            if min_flow > 0:
                network[v][i] -= min_flow
                network[i][v] += min_flow
                return min_flow

    return 0

max_flow = 0
while True:
    visited = [False] * (n + 1)

    flow = dfs(1, math.inf, visited, network)

    if flow == 0:
        break

    max_flow += flow

print(max_flow)