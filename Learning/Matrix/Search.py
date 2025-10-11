m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

# Is the same principle of binary search, divide in the middle
def search(matrix, target):
    l = 0
    r = len(matrix) - 1
    n = len(matrix[0]) - 1
    while l <= r:
        # Middle is l + r and not r - l
        m = (l + r) // 2
        if matrix[m][0] > target:
            r = m - 1
        elif matrix[m][n] < target:
            l = m + 1
        else:
            for i in range(n + 1):
                if matrix[m][i] == target:
                    return True
            return False
    return False

print(search(m, 5))