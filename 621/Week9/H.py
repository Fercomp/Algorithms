s = input().strip()
n = len(s)

d = [0] * n
for i in range(1, n):
    j = d[i-1]
    while j > 0 and s[i] != s[j]:
        j = d[j-1]

    if s[i] == s[j]:
        j += 1
    d[i] = j

borders = []
k = d[-1]

while k > 0:
    borders.append(k)
    k = d[k-1]
print(" ".join(map(str, sorted(borders))))