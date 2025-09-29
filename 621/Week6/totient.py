def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

n = int(input())
for _ in range(n):
    count = 0
    l = int(input())
    for i in range(l):
        g = gcd(i, l)
        if g == 1:
            count += 1
    print(count)