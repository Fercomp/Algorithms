# cses.fi/problemset/task/1193
n, m = map(int, input().split())
A, B = None, None
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
parents = [[-1] * m for _ in range(n)]

# TBD ...