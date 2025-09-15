# n, x = map(int, input().split())
# numbers = list(map(int, input().split()))

# m = n // 2
# l = numbers[:m]
# r = numbers[m:]

# d = {}
# for i in range(0, 2 ** m):
#     b = format(i, f"0{m}b")
#     s = sum([l[j] for j in range(len(b)) if b[j] == "1"])
#     d[s] = d.get(s, 0) + 1

# d2 = {}
# for i in range(0, 2 ** (n - m)):
#     b = format(i, f"0{n - m}b")
#     s = sum([r[j] for j in range(len(b)) if b[j] == "1"])
#     d2[s] = d2.get(s, 0) + 1
    
# count = 0
# for key, value in d.items():
#     target = x - key
#     count += value * d2.get(target, 0)

# print(count)


n, x = map(int, input().split())
numbers = list(map(int, input().split()))

m = n // 2
l = numbers[:m]
r = numbers[m:]

d = {}
for i in range(0, 2 ** m):
    s = 0
    for j in range(m):
        if i & (1 << j):
            s += l[j]
            
    d[s] = d.get(s, 0) + 1

d2 = {}
for i in range(0, 2 ** (n - m)):
    s = 0
    for j in range(n - m):
        if i & (1 << j):
            s += r[j]
    d2[s] = d2.get(s, 0) + 1
    
count = 0
for key, value in d.items():
    target = x - key
    count += value * d2.get(target, 0)

print(count)