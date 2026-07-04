n, x = map(int, input().split())
weights = sorted(list(map(int, input().split())))
l, r = 0, n-1

g = 0
while l <= r:
    g += 1
    if l == r:
        break
    
    if weights[l] + weights[r] <= x:
        l += 1
        r -= 1
        
    else:
        r -= 1
        
print(g)