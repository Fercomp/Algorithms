while True:
    try:
        n, s, j, d = map(int, input().split())
        row = input()
        idx = 0
        t_a, t_b = 0, 0
        while idx < n and t_a < s and t_b < s:
            a, b = 0, 0
            
            while True:
                if row[idx] == "A":
                    a += 1
                else:
                    b += 1
                idx += 1
                
                if (a >= j or b >= j) and abs(a - b) >= d:
                    if a > b:
                        t_a += 1
                    elif b > a:
                        t_b += 1
                        
                    break
        
        print(f"{t_a} {t_b}")
        
    except EOFError:
        break