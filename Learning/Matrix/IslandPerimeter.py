'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there
is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes", meaning the water inside
isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular,
width and height don't exceed 100. Determine the perimeter of the island.
'''

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

grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
print(islandPerimeter(grid))