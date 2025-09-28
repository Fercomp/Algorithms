import math
n = int(input())
l = list(map(int, input().split()))
m = math.ceil(n / 2)
l = sorted(l)
soma = sum(l[m:])
print(soma)