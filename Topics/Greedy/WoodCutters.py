n = int(input())
trees = [tuple(map(int, input().split())) for _ in range(n)]
if len(trees) == 1:
    print(1)
    exit()

count = 2
left = trees[0][0]
for i in range(1, n-1):
    if trees[i][0] - trees[i][1] > left:
        count += 1
        left = trees[i][0]
    elif trees[i][0] + trees[i][1] < trees[i+1][0]:
        count += 1
        left = trees[i][0] + trees[i][1]
    else:
        left = trees[i][0]

print(count)