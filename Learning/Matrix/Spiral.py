# https://leetcode.com/problems/spiral-matrix/

m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

def spiralOrder(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = []
    count = 0
    elements = n * m
    
    i, j = 0, 0
    while count < elements:
        while j < m:
            result.append(matrix[i][j])
            j+=1
            count+=1
        j-=1
        while i < n-1:
            i+=1
            result.append(matrix[i][j])
            count+=1
        while j > 0:
            j-=1
            result.append(matrix[i][j])
            count+=1
        while i > 1:
            i-=1
            result.append(matrix[i][j])
            count+=1
        n-=2
        m-=2
        j+=1
              
    return result

print(spiralOrder(m))