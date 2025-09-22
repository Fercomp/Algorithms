import sys

first = True
for line in sys.stdin:
    if not first:
        print()
    first = False

    n = int(line)
    l = input().split()
    d = {}
    for p in l:
        d[p] = 0
    
    for _ in range(n):
        line = input().split()
        a = line[0]
        m = int(line[1])
        number = int(line[2])

        if number != 0:
            d[a] += - m + m % number
        for g in range(3, len(line)):
            if number != 0:
                d[line[g]] += m // number
    
    for key, value in d.items():
        print(f"{key} {value}")