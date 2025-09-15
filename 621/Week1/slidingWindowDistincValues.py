n, k = map(int, input().split())
l = list(map(int, input().split()))

disc = 0
d = {}
result = []

for i in range(k):
    v = d.get(l[i], 0) + 1
    if v == 1:
        disc += 1        
    d[l[i]] = v
result.append(str(disc))

for i in range(k, len(l)):
    v = d.get(l[i - k]) - 1
    if v == 0:
        disc -= 1
    d[l[i - k]] = v
    
    u = d.get(l[i], 0) + 1
    if u == 1:
        disc += 1
    d[l[i]] = u
    result.append(str(disc))

print(" ".join(result))