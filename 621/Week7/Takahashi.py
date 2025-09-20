x, k, d = map(int, input().split())
x = abs(x)
d = abs(d)
q = x // d

if k > q:
    k -= q
    x -= q * d
    if k % 2 == 0:
        print(x)
    else:
        print(abs(x - d))
else:
    print(x - (k * d))