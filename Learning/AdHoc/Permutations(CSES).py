n = int(input())
if n == 2 or n == 3:
    print("NO SOLUTION")
    exit()
if n == 4:
    print("2 4 1 3")
    exit()
result = []
for i in range(1, n+1, 2):
    result.append(i)
for i in range(2, n+1, 2):
    result.append(i)
print(*result)