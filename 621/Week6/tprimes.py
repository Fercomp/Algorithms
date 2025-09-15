import math
n = int(input())
l = list(map(int, input().split()))

def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    limite = int(math.sqrt(x)) + 1
    for i in range(3, limite, 2):
        if x % i == 0:
            return False
    return True

for i in range(n):
    r = int(math.sqrt(l[i]))
    if r * r == l[i] and is_prime(r):
        print("YES")
    else:
        print("NO")