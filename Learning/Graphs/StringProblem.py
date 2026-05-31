# https://codeforces.com/problemset/problem/33/B

import math
string_a = list(input())
string_b = list(input())
graph = [[math.inf] * 26 for _ in range(26)]
n = int(input())

for _ in range(n):
    u, v, w = input().split()
    iu = ord(u) - ord('a')
    iv = ord(v) - ord('a')
    graph[iu][iv] = min(graph[iu][iv], int(w))
    
if len(string_a) != len(string_b):
    print(-1)
    exit()
    
for i in range(26):
    graph[i][i] = 0

for k in range(26):
    for i in range(26):
        for j in range(26):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
result = []
total = 0       
for i in range(len(string_a)):
    iv, iu = ord(string_a[i]) - ord('a'), ord(string_b[i]) - ord('a')
    current_sum = math.inf
    current_char = -1
    
    for c in range(26):
        cost = graph[iv][c] + graph[iu][c]

        if cost < current_sum:
            current_sum = cost
            current_char = c

    if current_sum == math.inf:
        print(-1)
        exit()

    total += current_sum
    result.append(chr(current_char + ord('a')))

print(total)
print("".join(result))