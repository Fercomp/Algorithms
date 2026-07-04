# https://leetcode.com/problems/spiral-matrix/

m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

def spiralOrder(matrix):
    left, right, up, bottom = 0, len(matrix[0]), 0, len(matrix)
    
    result = []
    while left <= right or bottom < up:
        for i in range(left, right):
            result.append(matrix[up][i])
        up += 1
        for i in range(bottom, up):
            result.append(matrix[i][right])
        right -= 1
        for i in range(right-1, left-1, -1):
            result.append(matrix[bottom-1][i])
        bottom -= 1
        for i in range(bottom-1, up-1, -1):
            result.append(matrix[i][left])
        left += 1
    return result

print(spiralOrder(m))