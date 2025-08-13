n, m = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(map(int, input().split()))
r = []

i = 0
j = 0
while i < n:
    while j < m and a[i] > b[j]:
        j += 1

    if j < m and a[i] == b[j]:
        i += 1
        j += 1
    else:
        r.append(str(a[i]))
        i += 1

print(" ".join(r))