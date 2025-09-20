n, x, m = map(int, input().split())

def a(n, m):
    if n < m:
        return n
    return  a((n - 1) ** 2, m) % m