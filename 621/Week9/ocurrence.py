n = str(input())
m = str(input())

a = len(n)
b = len(m)

ocurrence = [0] * b
j = 0
for i in range(1, b):
    while j > 0 and m[i] != m[j]:
        j = ocurrence[j-1]
    if m[i] == m[j]:
        j += 1
        ocurrence[i] = j

count = 0
j = 0
for i in range(a):
    while j > 0 and n[i] != m[j]:
        j = ocurrence[j-1]
    if n[i] == m[j]:
        j += 1
    if j == b:
        count += 1
        j = ocurrence[j-1]
        
print(count)