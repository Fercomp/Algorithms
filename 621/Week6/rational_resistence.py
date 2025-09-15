a, b = map(int, input().split())
if a > b:
    q = a // b
    r = a % b
    print(q + b)
else:
    print(b)