'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands. An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.
'''
from collections import deque
directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

def is_valid_cell(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def bfs(n, m, i, j, visited, grid):
    q = deque()
    q.append((i, j))
    while q:
        v = q.popleft()
        for direction in directions:
            x = int(v[0]) + direction[0]
            y = int(v[1]) + direction[1]
            if is_valid_cell(x, y, n, m) and (x, y) not in visited and grid[x][y] == "1":
                # It's very very important to add the cell when we first see it
                # because if we don't add we can visit it agai in a cycle, to see this try to
                # imagine what will happen in a complete graph, you will add all the vertices 
                # again in the second visit vertice
                visited.add((x, y))
                q.append((x, y))

def numIslands(grid):
    n,m = len(grid), len(grid[0])
    visited = set()
    island_count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1" and (i,j) not in visited :
                visited.add((i, j))
                bfs(n, m, i, j, visited, grid)
                island_count += 1
    return island_count

grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
print(numIslands(grid))