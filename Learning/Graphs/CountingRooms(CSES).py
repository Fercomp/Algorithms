# cses.fi/problemset/task/1192
from collections import deque

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(input()))

def is_valid(x, y):
    return 0 <= x < m and 0 <= y < n

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(x, y):
    grid[y][x] = "V"
    
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for d in directions:
            dx = d[0] + x
            dy = d[1] + y
            if is_valid(dx, dy) and grid[dy][dx] == ".":
                grid[dy][dx] = "V"
                queue.append((dx, dy))    

rooms = 0
for y in range(n):
    for x in range(m):
        if grid[y][x] == ".":
            bfs(x, y)
            rooms += 1
            
print(rooms)