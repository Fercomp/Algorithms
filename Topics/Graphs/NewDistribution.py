n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    row = list(map(int, input().split()))
    k = row[0]
    people = row[1:]

    for i in range(1, k):
        a = people[0]
        b = people[i]
        graph[a].append(b)
        graph[b].append(a)
        
from collections import deque
def bfs(graph, v):
    visited = set()
    queue = deque([v])
    while queue:
        u = queue.popleft()
        visited.add(u)
        for s in graph[u]:
            if s not in visited:
                queue.append(s)
    
    return len(visited)

result = []
for i in range(1, n+1):
    total_visited = bfs(graph, i)
    result.append(str(total_visited))

print(" ".join(result))