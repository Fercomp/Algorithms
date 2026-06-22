n, m, k = map(int, input().split())

desired = sorted(list(map(int, input().split())))
real = sorted(list(map(int, input().split())))

idx_d = 0
idx_r = 0
count = 0

#d = [10, 16, 34, 37, 46, 49, 56, 62, 69, 86]
#r = [7, 9, 43, 47, 50, 62, 71, 71, 83, 95]

while idx_d < n and idx_r < m:
    
    while idx_r < m and real[idx_r] - desired[idx_r] < 0:
        idx_r += 1
    
    if real[idx_r] - desired[idx_d] <= k:
        idx_r += 1
        idx_d += 1
        count += 1
    
    else:
        idx_d += 1
        
print(count)
    