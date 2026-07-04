directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def is_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def islandPerimeter(grid):
    n, m = len(grid), len(grid[0])
    perimeter = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                neighboors = 0
                for d in directions:
                    x = i + d[0]
                    y = j + d[1]
                    # The only catch is that if a cell has a neighbor, that side doesn’t count toward the perimeter. 
                    # A perimeter cell is always missing at least one neighbor.
                    if is_valid(x, y, n, m) and grid[x][y] == 1:
                        neighboors += 1
                perimeter += 4 - neighboors
    return perimeter