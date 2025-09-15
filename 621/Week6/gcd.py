def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)

a, b = map(int, input().split())
print(fac(min(a, b)))