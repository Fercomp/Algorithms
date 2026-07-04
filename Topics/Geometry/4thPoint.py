while True:
    try:
        input_l = input().split()
        if not input_l:
            break
            
        l = list(map(float, input_l))
    except EOFError:
        break

    p = []
    s = set()
    for i in range(0, len(l), 2):
        point = (l[i], l[i+1])
        if point in s:
            p.append((-2 * point[0], -2 * point[1]))
        else:
            p.append(point)
            s.add(point)
    
    final = [0, 0]
    for i in p:
        final[0] += i[0]
        final[1] += i[1]
    
    print(f"{final[0]:.3f} {final[1]:.3f}")