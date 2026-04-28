from collections import deque
n = int(input())
l = list(map(int, input().split()))
d = deque(l)
x, y, c = 0, 0, 1
while d:
    if d[0] > d[-1]:
        current = d.popleft()
    else:
        current = d.pop()
    
    if c == 1:
        x += current
    else:
        y += current
    c *= -1

print(x-y)