t = int(input())
for _ in range(t):
    n = int(input())
    result = []
    for _ in range(3):
        l = map(int, input().split())
        result.append(sorted([(v, i) for i, v in enumerate(l)], reverse=True)[:3])
    
    total_sum = 0
    for xa, a in result[0]:
        for xb, b in result[1]:
            for xc, c in result[2]:
                if a != b and b != c and a != c:
                    total_sum = max(total_sum, xa + xb + xc)   
        
    print(total_sum)