import math
sequenc = 0
while True:
    sequenc += 1
    n, m, c = map(int, input().split())
    if n == 0 and m == 0 and c == 0:
        break

    d = []
    for _ in range(n):
        ci = int(input())
        d.append(ci)
    
    toggles = [False] * n
    max_c = -math.inf 
    was_blown = False
    for j in range(m):
        i = int(input())
        if not was_blown:
            toggles[i-1] = not toggles[i-1]
            total = sum([d[i] for i in range(len(toggles)) if toggles[i] == True])
            max_c = max(max_c, total)

            if total > c:
                was_blown = True
    
    print(f"Sequence {sequenc}")
    if was_blown:
        print("Fuse was blown.")
    else:
        print("Fuse was not blown.")
        print(f"Maximal power consumption was {max_c} amperes.")
    print()