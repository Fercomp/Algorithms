import sys
class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:
            if self.size[rx] < self.size[ry]:
                rx, ry = ry, rx

            self.parents[ry] = rx
            self.size[rx] += self.size[ry]

it = iter(sys.stdin.buffer.read().split())
n = int(next(it))
m = int(next(it))
edges = []
can_be = [False] * m
for idx in range(m):
    a = int(next(it))
    b = int(next(it))
    w = int(next(it))
    edges.append((w, a, b, idx))

edges.sort()
uf = UnionFind(n)
i = 0
while i < m:
    j = i
    while j < m and edges[j][0] == edges[i][0]:
        j += 1

    for k in range(i, j):
        _, u, v, idx = edges[k]
        if uf.find(u) != uf.find(v):
            can_be[idx] = True

    for k in range(i, j):
        _, u, v, _ = edges[k]
        uf.union(u, v)
    i = j

out = []
for x in can_be:
    out.append("YES" if x else "NO")
sys.stdout.write("\n".join(out))