n = int(input())
l = list(map(int, input().split()))

max_sum = l[0]
current_sum = 0
for i in range(n):
    current_sum += l[i]
    max_sum = max(max_sum, current_sum)
    if current_sum < 0:
        current_sum = 0

print(max_sum)