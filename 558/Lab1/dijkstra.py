import math, heapq, statistics, time, utils

def dijkstra(n, source, destine, graph):
    dist = [math.inf] * n
    dist[source] = 0
    heap = [(0, source)]
    
    while heap:
        d, v = heapq.heappop(heap)
        if d > dist[v]:
            continue

        for w, u in graph[v]:
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                heapq.heappush(heap, (dist[u], u))

    return dist[destine]

tempos = []
for x in range(1, 16):
    n, m, c, s, d, graph = utils.create_graph(x)
    start = time.perf_counter()
    dijkstra(n, s, d, graph)
    end = time.perf_counter()
    interval = end - start
    print(f"Dijkstra n={n}, m={m}, c={c}, s={s}, d={d}, time={interval}")
    tempos.append(interval)
    
print("Média:", statistics.mean(tempos))