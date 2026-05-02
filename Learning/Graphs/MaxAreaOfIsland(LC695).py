# leetcode.com/problems/max-area-of-island

# Time: O(n * m)
# Space: O(n * m) due to call stack
def maxAreaOfIsland(grid):
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    n = len(grid)
    m = len(grid[0])

    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n and grid[y][x] == 1

    def dfs(i, j):
        # If we already have a grid is common to just set the (i, j) to 0
        # istead of hold a set of visited vertex, we don't need to use extra space
        grid[i][j] = 0
        count = 1
        for d in directions:
            x = j + d[0]
            y = i + d[1]
            if is_valid(x, y):
                count += dfs(y, x)
        return count
    
    max_area = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

    return max_area