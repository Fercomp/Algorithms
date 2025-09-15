from collections import deque, defaultdict

n = int(input())
g = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def bfs(start):
    q = deque([start])
    dist = [-1] * (n + 1)
    dist[start] = 0
    while q:
        u = q.popleft()
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    
    far = max(range(1, n+1), key=lambda x: dist[x])
    return far, dist[far]

a, _ = bfs(1)
b, diameter = bfs(a)
print(diameter)