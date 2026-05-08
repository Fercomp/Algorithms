import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

state = [0] * (n + 1)

def dfs(root, result):
    state[root] = 1

    for v in graph[root]:
        if state[v] == 1:
            print("IMPOSSIBLE")
            exit()

        if state[v] == 0:
            dfs(v, result)

    state[root] = 2
    result.append(root)

result = []
for i in range(1, n+1):
    if state[i] == 0:
        dfs(i, result)

result.reverse()
print(*result)