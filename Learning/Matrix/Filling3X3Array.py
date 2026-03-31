h1, h2, h3, w1, w2, w3 = map(int, input().split())
count = 0
for a in range(1, 31):
    for b in range(1, 31):
        for c in range(1, 31):
            for d in range(1, 31):
                r1 = h1 - a - b
                r2 = h2 - c - d
                r3 = w1 - a - c
                r4 = w2 - b - d
                
                r5 = h3 - r3 - r4
                r6 = w3 - r1 - r2
                if r1 > 0 and r2 > 0 and r3 > 0 and r4 > 0 and r5 > 0 and r5 == r6:
                    count += 1                            
print(count)