import math
import heapq
import time

def create_graph():
    graph = {}
    with open("graph.txt") as f:
        n, m, c = map(int, f.readline().split())
        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            graph.setdefault(u, []).append((w, v))
    return graph

def dijkstra(s=0):
    dist = [math.inf] * len(graph)
    dist[s] = 0
    heap = [(0, s)]
    
    while heap:
        d, v = heapq.heappop(heap)
        if d > dist[v]:
            continue

        for w, u in graph[v]:
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                heapq.heappush(heap, (dist[u], u))

    return dist

graph = create_graph()
print(dijkstra())

# import statistics, time
# tempos = []
# for _ in range(10):
#     start = time.perf_counter()
#     dijkstra()
#     end = time.perf_counter()
#     tempos.append(end - start)
    
# print("Média:", statistics.mean(tempos))
# print("Mediana:", statistics.median(tempos))
# print("Mínimo:", min(tempos))