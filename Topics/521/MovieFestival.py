n = int(input())

l = []
for i in range(n):
    d, f = map(int, input().split())
    l.append((d, f))

l.sort(key=lambda x: x[1])
end = 0
count = 0
for i in l:
    if i[0] >= end:
        end = i[1]
        count += 1

print(count)