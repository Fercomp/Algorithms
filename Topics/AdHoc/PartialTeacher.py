n = int(input())
l = list(input())

if l[0] == "=":
    result = [1, 1]
elif l[0] == "L":
    result = [2, 1]
else:
    result = [1, 2]

for i in range(1, n-1):
    if l[i] == "=":
        result.append(result[-1])
    if l[i] == "L":
        result.append(result[-1] -1)
    else:
        result.append(result[-1] +1)

m = min(result)
if m >= 1:
    print(" ".join(map(str, result)))
else:
    aux = 1 -m
    result = map(lambda x: x + aux, result)
    print(" ".join(map(str, result)))