class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:
            if self.size[rx] < self.size[ry]:
                rx, ry = ry, rx

            self.parents[ry] = rx
            self.size[rx] += self.size[ry]

edges = []
n, m = map(int, input().split())
union_find = UnionFind(n)

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
    
edges.sort()
cost = 0
for w, u, v in edges:
    if union_find.find(u) != union_find.find(v):
        union_find.union(u, v)
        cost += w
print(cost)