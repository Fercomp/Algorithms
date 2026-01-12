# Given a grid with and some queens marked as 1, return the safe spots in the board
# a safe spot is a cell that cannot be reached by any queen 

def is_safe(n, m, i, j):
    return 0 <= i < n and 0 <= j < m

def mark_reachable_cells(result, r, c):
    directions = [
        [-1, 0], [1, 0], [0, 1], [0, -1], # Horizontal / Vertical 
        [-1, -1], [1, -1], [-1, 1], [1, 1] # Diognal
        ]
    
    n = len(result)
    m = len(result[0])
    result[r][c] = 1
    for dir in directions:
        x = r + dir[0]
        y = c + dir[1]
        while is_safe(n, m, x, y):
            result[x][y] = 1
            x += dir[0]
            y += dir[1]   

# Time: O(n * m * queen_number)
def queensReach(board):
    n = len(board)
    m = len(board[0])
    
    result = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                mark_reachable_cells(result, i, j)
    
    return result