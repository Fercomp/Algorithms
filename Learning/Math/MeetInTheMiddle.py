from collections import Counter

n, x = map(int, input().split())
l = list(map(int, input().split()))

m = n // 2
l1 = l[:m]
l2 = l[m:]

d1 = {}
for i in range(2 ** len(l1)):
    mask = format(i, f"0{len(l1)}b")
    soma = sum([l1[b] for b in range(len(l1)) if mask[b] != "0"])
    d1[soma] = d1.get(soma, 0) + 1

d2 = {}
for i in range(2 ** len(l2)):
    mask = format(i, f"0{len(l2)}b")
    soma = sum([l2[b] for b in range(len(l2)) if mask[b] != "0"])
    d2[soma] = d2.get(soma, 0) + 1

count = 0
for key, value in d1.items():
    count += value * d2.get(x - key, 0)



from collections import Counter

n, x = map(int, input().split())
l = list(map(int, input().split()))

m = n // 2
l1 = l[:m]
l2 = l[m:]

d1 = Counter()
for i in range(1 << len(l1)):
    soma = 0
    for j in range(len(l1)):
        if i & (1 << j):
            soma += l1[j]
    d1[soma] += 1

d2 = Counter()
for i in range(1 << len(l2)):
    soma = 0
    for j in range(len(l2)):
        if i & (1 << j):
            soma += l2[j]
    d2[soma] += 1

count = 0
for s1, c1 in d1.items():
    count += c1 * d2.get(x - s1, 0)

print(count)

print(count)