n = int(input())
dans = list(map(int, input().split()))

count = 0
m = 1
for d in dans:
    count += d * m
    m *= -1
    
r = [count]
for i in range(1, n):
    x = 2 * dans[i-1] - r[-1]
    r.append(x)

print(" ".join(map(str, r)))