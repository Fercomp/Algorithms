n, m = map(int, input().split())
graph = { i: [] for i in range(1, n+1) }

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(root, teams):
    teams[root] = 1

    stack = [root]
    while stack:
        v = stack.pop()

        for u in graph[v]:
            if teams[u] == -1:
                curr_team = 2 if teams[v] == 1 else 1
                teams[u] = curr_team
                stack.append(u)
                
            if teams[u] == teams[v]:
                return False
            
    return True

teams = [-1] * (n+1)
for i in range(1, n+1):
    if teams[i] == -1:
        if not dfs(i, teams):
            print("IMPOSSIBLE") 
            exit()

print(*teams[1:])