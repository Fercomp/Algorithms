# leetcode.com/problems/rotting-oranges

from collections import deque
# Time: O(n * m)
# Space: O(n * m) due to queue
def orangesRotting(grid):
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    n = len(grid)
    m = len(grid[0])
    
    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n and grid[y][x] == 1

    # Trick: count the number of fresh oranges during the first pass
    # so we don't need to scan the grid again later
    fresh = 0
    queue = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((j, i))
            if grid[i][j] == 1:
                fresh += 1

    time = -1
    while queue:
        for j in range(len(queue)):
            v = queue.popleft()
            for d in directions:
                x = v[0] + d[0]
                y = v[1] + d[1]
                if is_valid(x, y):
                    fresh -= 1
                    grid[y][x] = 2
                    queue.append((x, y))
        time += 1
    
    # If there are still fresh oranges, it means some were unreachable
    if fresh != 0:
        return -1

    return max(0, time)