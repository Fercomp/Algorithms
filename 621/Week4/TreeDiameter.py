from collections import defaultdict
n = int(input())
tree = defaultdict(list)

for _ in range(n-1):
    v, u = map(int, input().split())
    tree[v].append(u)

dim = 0
def height(t, r):
    if not t[r]:
        return 0
    
    h = 0
    for v in t[r]:
        he = height(t, v)
        global dim
        dim = max(dim, he + h)
        h = max(h, he)
    return h + 1
height(tree, 1)  
print(dim)