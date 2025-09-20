n, m = map(int, input().split())
d1 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
d2 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

q = n // 5
r = n % 5
for key in d1.keys():
    d1[key] = q
for i in range(1, r+1):
    d1[i] += 1

q = m // 5
r = m % 5
for key in d2.keys():
    d2[key] = q
for i in range(1, r+1):
    d2[i] += 1

count = 0
for key, value in d1.items():
    target = (5 - key) % 5
    a = d2[target]
    count += value * a

print(count)