import math
n = int(input())
woods = []
for _ in range(n):
    x, h = map(int, input().split())
    woods.append((x, h))

total_of_trees = 0
l, r = 0, len(woods)-1
left_bound, right_bound = -math.inf, math.inf
is_left = True

while l <= r:
    if is_left:
        if woods[l][0] - woods[l][1] > left_bound:
            total_of_trees += 1
            left_bound = woods[l][0]
        l += 1
    else:
        if woods[r][0] + woods[r][1] < right_bound:
            total_of_trees += 1
            right_bound = woods[r][0]
        r -= 1
        
    is_left = not is_left

print(total_of_trees)