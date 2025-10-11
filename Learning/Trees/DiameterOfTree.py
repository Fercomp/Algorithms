from collections import defaultdict
n = int(input())
d = defaultdict(list)
for i in range(n-1):
    u, v = map(int, input().split())
    d[u].append(v)

res = 0
def height_of_tree(root):
    global res
    if not root:
        return 0
    
    max_height = 0
    max_height_2 = 0
    for v in d[root]:
        h = height_of_tree(v) + 1
        if h > max_height:
            max_height_2 = max_height
            max_height = h
        elif h > max_height_2:
            max_height_2 = h
        res = max(res, max_height + max_height_2)
    return max_height

height_of_tree(1)
print(res)

#
# from collections import deque, defaultdict

# n = int(input())
# g = defaultdict(list)
# for _ in range(n-1):
#     a, b = map(int, input().split())
#     g[a].append(b)
#     g[b].append(a)

# def bfs(start):
#     q = deque([start])
#     dist = [-1] * (n + 1)
#     dist[start] = 0
#     while q:
#         u = q.popleft()
#         for v in g[u]:
#             if dist[v] == -1:
#                 dist[v] = dist[u] + 1
#                 q.append(v)
#     # acha nó mais distante e distância
#     far = max(range(1, n+1), key=lambda x: dist[x])
#     return far, dist[far]

# a, _ = bfs(1)
# b, diameter = bfs(a)
# print(diameter)