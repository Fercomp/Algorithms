# 0
# |\
# 1 \
# |\ |
# 2 3
# |
# 4

graph = [[1, 3], [2, 3], [1,4], [1,2], [2]]
from collections import deque
def DFS(g):
    v = [False] * len(g)

    for i in range(len(v)):
        if not v[i]:
            DFS_visit(g, v, i)


def DFS_visit(g, v, i):
    v[i] = True
    print(i)
    for u in g[i]:
        if not v[u]:
            DFS_visit(g, v, u)

DFS(graph)