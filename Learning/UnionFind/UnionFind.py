class UnionFind:
    def __init__(self, n):
        # Initially, every element is its own parent (each element is its own set)
        self.parents = list(range(n + 1))
        # Size of each tree (used for union by size)
        # Initially every set contains only one element
        self.size = [1] * (n + 1)

    # O(α(n)) amortized
    # returns the representative (root) of the set containing x
    def find(self, x):
        # Uses path compression: while finding the root, we update the parent
        # of each visited node to point directly to the root. This keeps the
        # trees shallow and speeds up future operations.
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    # O(α(n)) amortized
    # Merges the sets containing x and y.
    def union(self, x, y):
        # Uses union by size: the smaller tree is attached under the root
        # of the larger tree. This helps prevent the trees from becoming tall.
        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:
            # Attach the smaller tree under the larger tree
            if self.size[rx] < self.size[ry]:
                rx, ry = ry, rx

            self.parents[ry] = rx
            self.size[rx] += self.size[ry]