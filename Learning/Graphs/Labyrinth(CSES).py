# cses.fi/problemset/task/1193
from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
dir = [[1, 0, "R"], [-1, 0, "L"], [0, 1, "D"], [0, -1, "U"]]
parent = [[None] * m for _ in range(n)]

def is_valid(x, y):
    return 0 <= x < m and 0 <= y < n

for y in range(n):
    for x in range(m):
        if grid[y][x] == "A":
            A = [x, y]
            
        elif grid[y][x] == "B":
            B = [x, y]

queue = deque([A])
ax, ay = A
grid[ay][ax] = "#"
found = False

while queue:
    x, y = queue.popleft()

    if [x, y] == B:
        found = True
        break

    for dx, dy, move in dir:
        nx = x + dx
        ny = y + dy

        if is_valid(nx, ny) and grid[ny][nx] != "#":
            parent[ny][nx] = (x, y, move)
            queue.append((nx, ny))
            grid[ny][nx] = "#"

if not found:
    print("NO")

else:
    path = []
    x, y = B
    while [x, y] != A:
        px, py, move = parent[y][x]
        path.append(move)
        x, y = px, py

    path.reverse()
    print("YES")
    print(len(path))
    print("".join(path))