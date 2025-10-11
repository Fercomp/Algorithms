# Function to know if the neighboor of the cell is valid 
def is_safe(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

# All the four directions of possible neighbor a cell can have
directions = [[1,0], [0,1], [-1,0], [0,-1]]

from collections import deque
def rotten_oranges(g):
    n, m = len(g), len(g[0])

    q = deque()
    for i in range(n):
        for j in range(m):
            if g[i][j] == 2:
                q.append((i, j))

    elapsed_time = 0
    while q:
        elapsed_time += 1

        for _ in range(len(q)):
            v, u = q.popleft()
            for d in directions:
                x = v + d[0]
                y = u + d[1]

                if is_safe(x, y, n, m) and g[x][y] == 1:
                    g[x][y] = 2
                    q.append((x, y))

    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                return -1

    return elapsed_time

mat = [[2, 1, 0, 2, 1],
       [1, 0, 1, 2, 1],
       [1, 0, 0, 2, 1]]

print(rotten_oranges(mat))