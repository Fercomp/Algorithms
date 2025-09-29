import math
n = int(input())
l = list(map(int, input().split()))

def is_tprime(x):
    if x == 1:
        return False
    r = math.sqrt(x)
    if r * r == x:
        return True
    else:
        return False

for i in l:
    if is_tprime(i):
        print("YES")
    else:
        print("NO")