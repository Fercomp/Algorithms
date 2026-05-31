from collections import deque
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(input().strip()))

directions = [1, 0], [-1, 0], [0, 1], [0, -1]    
graph_of_paintings = [[0] * m for _ in range(n)]

comp_id = 0
id_to_cost = {}
def bfs(x, y, comp_id):
    paintings = 0
    queue = deque([(x, y)])
    graph_of_paintings[y][x] = comp_id
    graph[y][x] = "#"
    
    while queue:
        x, y = queue.popleft()
        
        for d0, d1 in directions:
            dx, dy = x + d0, y + d1
            
            if graph[dy][dx] == "*":
                paintings += 1
                
            elif graph[dy][dx] == ".":
                graph[dy][dx] = "#"
                queue.append((dx, dy))
                graph_of_paintings[dy][dx] = comp_id
    
    return paintings

for y in range(n):
    for x in range(m):
        if graph[y][x] == ".":
            comp_id += 1
            paitings = bfs(x, y, comp_id)
            id_to_cost[comp_id] = paitings

result = []
for _ in range(k):
    y, x = map(int, input().split())
    result.append(str(id_to_cost[graph_of_paintings[y-1][x-1]]))
sys.stdout.write("\n".join(result))