import math
def helper(days, x, used, d):
    key = (x, tuple(used))
    if key in d:
        return d[key]
    if all(used):
        return 0
    if x < 0:
        return -math.inf
    
    max_friends = -math.inf
    for i in range(3):
        if not used[i]:
            used[i] = True
            friends = days[i][x] + helper(days, x-1, used, d)
            max_friends = max(max_friends, friends)
            used[i] = False
    max_friends = max(max_friends, helper(days, x-1, used, d))
    d[key] = max_friends
    return max_friends

t = int(input())
for _ in range(t):
    n = int(input())
    days = []
    for i in range(3):
        day = list(map(int, input().split()))
        days.append(day)

    used = [False] * 3
    d = {}
    print(helper(days, n-1, used, d))