# Very important library that have deque usuful to work like a queue
from collections import deque

def bfs(adj):
    s = 2
    t = []

    visited = [False] * len(adj)
    visited[s] = True

    q = deque()
    q.append(s)

    while q:
        u = q.popleft()
        for i in adj[u]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

        t.append(u)
    return t
print(bfs([[2],[2],[0,1,3],[2]]))
