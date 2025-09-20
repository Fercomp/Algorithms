n, k = map(int, input().split())
count = 0

for i in range(k, n+1):
    if k > i:
        continue
    q = n // i
    r = n % i
    count += (i - k) * q + max(0, r - k + 1)
print(count)