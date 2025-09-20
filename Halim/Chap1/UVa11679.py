while True:
    b, n = map(int, input().split())
    if b == 0 and n == 0:
        break
    
    dic = {}
    banks = list(map(int, input().split()))
    for i in range(len(banks)):
        dic[i + 1] = banks[i]
    
    for i in range(n):
        d, c, v = map(int, input().split())
        dic[d] -= v
        dic[c] += v
    
    p = all(value >= 0 for value in dic.values())
    print("S" if p else "N" )