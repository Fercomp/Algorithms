# It's important to know how to traverse a graph with adjancency matrix

from collections import deque
def bfs_matrix(m, s=0):
    n = len(m)
    q = deque()
    q.append(s)
    v = [False] * n
    v[s] = True
    t = []

    while q:
        u = q.popleft()
        t.append(u)

        for i in range(n):
            if m[u][i] == 1 and not v[i]:
                v[i] = True
                q.append(i)
    
    return t

graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

print(bfs_matrix(graph))