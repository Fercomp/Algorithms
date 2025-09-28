n, m, c = map(int, input().split())
board = []
for _ in range(n):
    r = list(input())
    board.append(r)

dirr = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1), (1, 1), (-1, 1)]
next_board = [[0] * m for _ in range(n)]

for _ in range(c):
    for i in range(n):
        for j in range(m):
            neighboors = 0
            for d in dirr:
                x = (i + d[0]) % n
                y = (j + d[1]) % m
                if board[x][y] == "*":
                    neighboors += 1
            
            if board[i][j] == "*" and (neighboors == 2 or neighboors == 3):
                next_board[i][j] = "*"
            elif board[i][j] == "-" and neighboors == 3:
                next_board[i][j] = "*"
            else:
                next_board[i][j] = "-"

    board, next_board = next_board, board

for i in range(n):
    print("".join(board[i]))