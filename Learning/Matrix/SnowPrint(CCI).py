M = [
    [0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
    ]

def first_paw(M, i):
    for j in range(len(M)):
        if M[j][i] == 1:
            return j
    return -1

import math
# Naive implementation for each colum m we need to see all the n rows
# So time complexity is O(m * n)
def snow_print(M):
    min_paw = math.inf
    for i in range(len(M[0])):
        min_paw = min(first_paw(M, i), min_paw)
    return min_paw


def is_valid(n, m, i, j):
    return 0 <= i < n and 0 <= j < m

# The best aproach is for each collum we check only the 3 neighboors 
# so the time complexity is O(c * m) = O(m)
def snow_print2(M):
    directions = [[1, 0], [1, -1], [1, 1]]
    start_paw = 0
    for i in range(len(M)):
        if M[i][0] == 1:
            start_paw = i
    
    minimum_paw = start_paw
    current_paw = start_paw
    for i in range(len(M[0])-1):
        for dir in directions:
            x = i + dir[0]
            y = current_paw + dir[1]
            if is_valid(len(M[0]), len(M), x, y) and M[y][x] == 1:
                minimum_paw = min(minimum_paw, y)
                current_paw = y
    return minimum_paw
        
print(snow_print2(M))