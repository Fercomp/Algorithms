# cses.fi/problemset/task/1094
n = int(input())
nums = list(map(int, input().split()))

total = 0
for i in range(len(nums)):
    if i > 0:
        desired_value = max(nums[i], nums[i-1])
        total += desired_value - nums[i]
        nums[i] = desired_value

print(total)