from collections import deque

n, m = 4, 2
graph = {
    1: [2, 3],
    2: [],
    3: [4],
    4: []
    }

visited = [False] * (n + 1)
parent = [-1] * (n + 1)

def bfs(root):
    visited[root] = True
    q = deque()
    q.append(root)

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                parent[i] = v