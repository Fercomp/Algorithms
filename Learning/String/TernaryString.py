import math
t = int(input())
for _ in range(t):
    s = input()
    i1 = math.inf
    i2 = math.inf
    i3 = math.inf
    min_d = math.inf
    for i in range(len(s)):
        if s[i] == "1":
            i1 = i
        elif s[i] == "2":
            i2 = i
        else:
            i3 = i
        
        d = max(i1, i2, i3) - min(i1, i2, i3) + 1
        min_d = min(min_d, d)
        
    print(min_d if min_d != math.inf else 0)
    
# 1112322