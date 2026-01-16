# hackerrank.com/challenges/2d-array

import math
M = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9,  0,  4, 3, 2],
    [-9, -9, -9,  1, 2, 3],
    [0,  0,  8,  6, 6, 0],
    [0,  0,  0, -2, 0, 0],
    [0,  0,  1,  2, 4, 0]
    ]

hour_glass_mask = [
    [0, 0], [1, 0], [2, 0]
          , [1, 1],
    [0, 2], [1, 2], [2, 2]
    ]

def hourglassSum(arr):
    n = len(arr)
    m = len(arr[0])
    if n < 3 or m < 3:
        return 0
    
    max_sum = -math.inf
    for i in range(n -2):
        for j in range(m -2):
            cur_sum = 0
            for dir in hour_glass_mask:
                # Is very important to notice that i control the y axis and j the x axis
                # so is i + dir[1] that if the y and j + dir[0] that is the x
                cur_sum += arr[i + dir[1]][j + dir[0]]
            max_sum = max(max_sum, cur_sum)
            
    return max_sum

print(hourglassSum(M))