matrix = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
]

def is_last(m, i, j):
    if j == 0:
        return True
    if m[i][j - 1] == 0:
        return True    
    return False


def linear_search(m):
    n = len(matrix)
    m = len(matrix[0])

    r = 0
    maxi = (-1, -1)
    for i in range(m - 1, -1, -1):
        if matrix[r][i] == 1 and is_last(matrix, r, i):
            maxi = (r, i)

            for _ in range(r + 1, n):
                r += 1
                if matrix[r][i] == 1:
                    break
    print(maxi)