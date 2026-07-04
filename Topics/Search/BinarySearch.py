import math
# i  0  1  2  3  4  5  
n = [1, 2, 2, 4, 9, 13]
t = 4

l = 0
r = len(n) - 1
result = -1

while l <= r:
    m = math.floor((r + l) / 2)
    if n[m] < t:
        l = m + 1
    elif n[m] > t:
        r = m -1
    else:
        result = m
        break
        
print(result)
