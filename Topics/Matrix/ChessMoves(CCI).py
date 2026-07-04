# Return a list of all the unoccupied cells in board that can be reached by the given piece
# in one move, starting from (r, c)

def is_valid(n, m, r, c):
    return 0 <= r < n and 0 <= c < m
    
def free_king_cells(board, r, c):
    directions = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
    n = len(board)
    m = len(board[0])
    for dir in directions:
        x = r + dir[0]
        y = c + dir[1]
        if is_valid(n, m, x, y) and board[x][i] == 0:
            board[x][y] = 1
    
    result = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                result.append([i, j])

    return result 

def free_horse_cells(board, r, c):
    directions = [[-2, -1], [2, -1], [1, -2], [-1, -2], [-2, 1], [2, 1], [1, 2], [-1, 2]]
    n = len(board)
    m = len(board[0])
    for dir in directions:
        x = r + dir[0]
        y = c + dir[1]
        if is_valid(n, m, x, y) and board[x][i] == 0:
            board[x][y] = 1
    
    result = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                result.append([i, j])

    return result 

def free_queen_cells(board, r, c):
    directions = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
    n = len(board)
    m = len(board[0])
    for dir in directions:
        x = r + dir[0]
        y = c + dir[1]
        while is_valid(n, m, x, y) and board[x][i] == 0:
            board[x][y] = 1
            x += dir[0]
            y += dir[1]
    
    result = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                result.append([i, j])

    return result 

def chess_move(board, r, c, piece):
    if piece == "king":
        return free_king_cells(board, r, c, piece)
    elif piece == "horse":
        return free_horse_cells(board, r, c, piece)
    elif piece == "queen":
        return free_queen_cells(board, r, c, piece)