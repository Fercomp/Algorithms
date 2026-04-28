import math
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    total = 0
    signal = 1 if l[0] > 0 else -1
    best = l[0]
    for i in range(1, n):
        if l[i] > 0 and signal == 1:
            best = max(best, l[i])
        
        elif l[i] > 0 and signal == -1:
            total += best
            best = l[i]
            signal = 1
        
        elif l[i] < 0 and signal == -1:
            best = max(best, l[i])
        
        else:
            total += best
            best = l[i]
            signal = -1
    
    total += best
    print(total)