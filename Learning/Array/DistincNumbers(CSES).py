# https://cses.fi/problemset/task/1621/
n = int(input())
line = list(map(int, input().split()))
line.sort()

count = 1
for i in range(1, n):
    if line[i] != line[i-1]:
        count += 1

print(count)