# https://cses.fi/problemset/task/1680
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

graph = defaultdict(list)
n, m = map(int, input().split())
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

top_sort = []
visited = [0] * (n + 1)
def dfs(root):
    visited[root] = 1
    for v in graph[root]:
        if not visited[v]:
            dfs(v)
    top_sort.append(root)
    
dfs(1)
top_sort.reverse()
parents = [-1] * (n + 1)
cities_num = [0] * (n + 1)
cities_num[1] = 1

for i in top_sort:
    if cities_num[i] == 0:
        continue
    
    for v in graph[i]:
        if cities_num[i] + 1 > cities_num[v]:
            cities_num[v] = cities_num[i] + 1
            parents[v] = i

if cities_num[n] == 0:
    print("IMPOSSIBLE")
    exit()
            
current = n
result = []
while current != -1:
    result.append(current)
    current = parents[current]
    
result.reverse()
print(cities_num[n])
print(*result)