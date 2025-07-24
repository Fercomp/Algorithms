matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def print_matrix(matrix):
    n, m = len(matrix), len(matrix[0])

    for i in range(n):
        for j in range(m):
            print(matrix[i][j])

def print_matrix2(matrix, i, j):
    m, n = (len(matrix) - 1), (len(matrix[0]) - 1)

    if i > m:
        return

    print(matrix[i][j])

    if j >= n:
        print_matrix2(matrix, i+1, 0)
    else:
        print_matrix2(matrix, i, j+1)

print_matrix2(matrix, 0, 0)