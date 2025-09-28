n, k = map(int, input().split())
count = 0

for i in range(k, n):
    count += n - i + (i // k)

print(count)