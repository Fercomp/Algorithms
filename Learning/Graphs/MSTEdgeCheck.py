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

n, m = map(int, input().split())

edges = []
can_be = [False] * m
for i in range(m):
    a, b, w = map(int, input().split())
    edges.append((w, a, b, i))

union_find = UnionFind(n)
edges.sort()

i = 0
while i < len(edges): 
    j = i
    while j < len(edges) and edges[i][0] == edges[j][0]:
        j+=1
    
    for x in range(i, j):
        w, a, b, idx = edges[x]
        if union_find.find(a) != union_find.find(b):
            can_be[idx] = True
    
    for x in range(i, j):
        _, a, b, _ = edges[x]
        union_find.union(a, b)
    i = j

for y in can_be:
    print("YES" if y else "NO")