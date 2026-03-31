class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n+1))
        self.size = [1] * (n+1)

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

n, m = map(int, input().split())
uf = UnionFind(n)

for _ in range(m):
    row = list(map(int, input().split()))
    k = row[0]

    if k > 0:
        first = row[1]
        for i in range(2, k+1):
            uf.union(first, row[i])

result = []
for i in range(1, n+1):
    total_people = uf.find(i)
    result.append(str(uf.size[total_people]))
print(" ".join(result))