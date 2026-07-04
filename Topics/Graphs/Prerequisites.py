import sys
sys.setrecursionlimit(10**6)
n = int(input())
graph = {i: [] for i in range(1, n + 1)}

for i in range(1, n + 1):
    inp = list(map(int, input().split()))
    graph[i] = inp[1:]

visited = [False] * (n + 1)
def dfs(root, result):
    visited[root] = True
    for v in graph[root]:
        if not visited[v]:
            dfs(v, result)
    result.append(root)

result = []
dfs(1, result)
result.pop()
print(*result)