from collections import deque
def updateMatrix(mat):
    q = deque()
    n, m = len(mat), len(mat[0])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                q.append((j, i))
            else:
                mat[i][j] = -1
    
    distance = 1
    while q:
        for _ in range(len(q)):
            cell = q.popleft()
            for d in directions:
                x, y = cell[0] + d[0], cell[1] + d[1]
                if is_valid(x, y) and mat[y][x] == -1:
                    q.append((x, y))
                    mat[y][x] = distance
        distance += 1
    
    return mat
