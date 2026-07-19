n, m, k = map(int, input().split())
desired = sorted(list(map(int, input().split())))
real = sorted(list(map(int, input().split())))
idx_d, idx_r, count = 0, 0, 0

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
    