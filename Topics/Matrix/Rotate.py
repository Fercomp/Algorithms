matrix = [[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]]

n, m = len(matrix), len(matrix[0])

for i in range(n):
    for j in range(i+1, m):
        aux = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = aux

middle = m // 2
for i in range(middle):
    for j in range(n):
        aux = matrix[j][m - i - 1]
        matrix[j][m-i-1] = matrix[j][i]
        matrix[j][i] = aux
        
print(matrix)