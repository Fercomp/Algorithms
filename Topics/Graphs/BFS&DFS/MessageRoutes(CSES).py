from collections import deque
n, m = map(int, input().split())
graph = { i: [] for i in range(1, n+1) }

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [-1] * (n + 1)

def bfs(parent):
    parent[1] = 0
    queue = deque([1])

    while queue:
        for _ in range(len(queue)):
            v = queue.popleft()

            for u in graph[v]:
                if parent[u] == -1:

                    queue.append(u)
                    parent[u] = v
                    if u == n:
                        return 1
                
    return -1

is_reachable = bfs(parent)
if is_reachable == -1:
    print("IMPOSSIBLE") 
    exit()

result = []
curr = n
while curr != 0:
    result.append(curr)
    curr = parent[curr]

result.reverse()
print(len(result))
print(*result)