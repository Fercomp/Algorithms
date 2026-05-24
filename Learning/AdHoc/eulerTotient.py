t = int(input())
q = []
for _ in range(t):
    q.append(int(input()))
maxq = max(q)
t = [0] * (maxq + 1)
for i in range(maxq+ 1):
    t[i] = i

p = 2
while p <= maxq:
    if t[p] == p:
        j = p
        while j <= maxq:
            t[j] -= t[j] // p
            j += p
    p += 1

if maxq >= 1:
    t[1] = 1
for x in q:
    print(t[x])