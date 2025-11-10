s = str(input())
n = len(s)
p = [0] * n
j = 0
for i in range(1, n):
    while j > 0 and s[i] != s[j]:
        j = p[j - 1]
    if s[i] == s[j]:
        j += 1
    p[i] = j

borda = []
k = p[n - 1]
while k > 0:
    borda.append(k)
    k = p[k - 1]
ans = []
for b in borda:
    ans.append(str(n - b))
ans.append(str(n))  
print(" ".join(ans))