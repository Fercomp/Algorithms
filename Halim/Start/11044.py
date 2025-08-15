t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    n, m = n-2, m-2
    q1 = n // 3
    r1 = n % 3
    if r1 > 0:
        q1 += 1
    
    q2 = m // 3
    r2 = m % 3
    if r2 > 0:
        q2 += 1
    
    print(q1 * q2)