# leetcode.com/problems/valid-sudoku

# First way -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Simple approach: iterate through all rows, then all columns,
# and finally all 3x3 sub-grids
# Time: O(3 * 9^2) three full passes over the board
# Space: O(9) at most one set of size 9 is used at a time
# after each check, the set is discarded and reused
def isValidSudoku1(board):
    for i in range(9):
        my_set = set()
        for j in range(9):
            if board[i][j] != ".":
                if board[i][j] not in my_set:
                    my_set.add(board[i][j])
                else:
                    return False
    
    for i in range(9):
        my_set = set()
        for j in range(9):
            if board[j][i] != ".":
                if board[j][i] not in my_set:
                    my_set.add(board[j][i])
                else:
                    return False
    
    def checkSquare(list, l, c):
        my_set = set()
        for i in range(l, l+3):
            for j in range(c, c+3):
                if list[i][j] != ".":
                    if list[i][j] not in my_set:
                        my_set.add(list[i][j])
                    else:
                        return False
        return True

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not checkSquare(board, i, j):
                return False
    
    return True

# Second way -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# I will create three dictionaries one for the rows, one for the columns,
# and one for the blocks. I will iterate over the board only once, and in
# each iteration I will update all three structures
# Time: O(3 * 9^2) only one loop over the board, but three constant-time
# operations are performed for each cell
# Space: O(3 * 9^2) Three dictionaries are maintained at the same time,
# and each key can store up to 9 different values

from collections import defaultdict
def isValidSudoku2(board):
    lines = defaultdict(set)
    rows = defaultdict(set)
    blocks = defaultdict(set)
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            
            if (board[i][j] in lines[i] or 
                board[i][j] in rows[j] or 
                board[i][j] in blocks[(i // 3, j // 3)]):
                return False
            else:
                lines[i].add(board[i][j])
                rows[j].add(board[i][j])
                blocks[(i // 3, j // 3)].add(board[i][j])
    
    return True