# https://vjudge.net/problem/DMOJ-ccc14j3
antonia_points = 100
david_points = 100
n = int(input())
for _ in range(n):
    a, d = map(int, input().split())
    if a == d:
        continue
    if a > d:
        david_points = max(0, david_points -a)
    if d > a:
        antonia_points = max(0, antonia_points -d)

print(antonia_points)
print(david_points)