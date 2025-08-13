import heapq

t = int(input())
for i in range(t):
    n, m, x, y = map(int, input().split())
    dic = {i : [] for i in range(1, n+1)}
    for j in range(m):
        v, e = map(int, input().split())
        dic[v].append(e)
        dic[e].append(v)

    t = [False] * (n + 1)
    t[x] = True
    q = []
    heapq.heappush(q, x)
    r = []
    while q:
        v = heapq.heappop(q)
        r.append(str(v))
        if v == y:
            break

        for u in dic[v]:
            if not t[u]:
                heapq.heappush(q, u)
                t[u] = True
    print(" ".join(r))