# leetcode.com/problems/set-matrix-zeroes/

# Naive Solution / Brute Force
# Time: O(n.m.(n + m))
# Space: O(1)
def setZeroes1(matrix):
    # [x, y]
    directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

    def set_dir(d, i, j, n, m):
        y, x = i + d[1], j + d[0]
        while x < m and y < n and matrix[y][x] != 0:
            matrix[y][x] = None
            y += d[1]
            x += d[0]

    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                for d in directions:
                    set_dir(d, i, j, n, m)
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == None:
                matrix[i][j] = 0
       
# Better approach
# Time: O(n*m + 2*n*m) = O(n*m)
# Space: O(n + m)
def setZeroes2(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rows = [0] * n
    colls = [0] * m
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                rows[i] = 1
                colls[j] = 1
                
    for i in range(n):
        if rows[i] == 1:
            for j in range(m):
                matrix[i][j] = 0
                
    for j in range(m):
        if colls[j] == 1:
            for i in range(n):
                matrix[i][j] = 0
          
          
def setZeroes3(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(0, n):
        for j in range(0, m):
            if i + j > 0 and matrix[i][j] == 0 :
                if i != 0 and j != 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                
    for i in range(1, n):
        if matrix[i][0] == 0:
            for j in range(1, m):
                matrix[i][j] = 0
                
    for j in range(1, m):
        if matrix[0][j] == 0:
            for i in range(n):
                matrix[i][j] = 0
                
    if matrix[0][0] == 0:
        matrix[0] = [0] * m
        for i in range(n):
            matrix[i][0] = 0
    
matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes3(matrix)
print(matrix) # [[1,0,1],[0,0,0],[1,0,1]]