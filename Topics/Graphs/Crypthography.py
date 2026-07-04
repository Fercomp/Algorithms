import math
str1 = input()
str2 = input()

graph = [[math.inf] * (127) for _ in range(127)]

n = int(input())
for i in range(n):
    a, b, c = input().split()
    graph[ord(a)][ord(b)] = min(graph[ord(a)][ord(b)], int(c))

for i in range(127):
    graph[i][i] = 0

for k in range(0, 127):
    for i in range(0, 127):
        for j in range(0, 127):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

soma = 0
for i in range(len(str1)):
    soma += graph[ord(str1[i])][ord(str2[i])]
    if soma == math.inf:
        print(-1)
        exit()

print(soma)