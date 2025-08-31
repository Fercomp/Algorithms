import sys
from collections import defaultdict
import time

def create_graph():
    graph = {}
    with open("graph.txt") as f:
        n, m, c = map(int, f.readline().split())
        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            graph.setdefault(u, []).append((w, v))
    return n, m, c, graph

def fastDijkstra(s=0):
    dist = [sys.maxsize] * len(graph)
    dist[s] = 0

    maxDist = (n - 1) * c
    buckets = defaultdict(set)
    buckets[0].add(s)
    
    bucket_pointer = 0
    while buckets:
        # enquanto não achar um bucket existente ou bucket exista mas tenha algo dentro
        while bucket_pointer not in buckets or not buckets[bucket_pointer]:
            bucket_pointer += 1
            if bucket_pointer > maxDist:
                break
        if bucket_pointer > maxDist:
            break
        
        u = buckets[bucket_pointer].pop()
        # Se for o último elemento do bucket delete ele
        if not buckets[bucket_pointer]:
            del buckets[bucket_pointer]

        for w, v in graph[u]:
            newDist = dist[u] + w
            if newDist < dist[v]:
                if dist[v] != sys.maxsize:
                    buckets[dist[v]].discard(v)
                    if not buckets[dist[v]]:
                        del buckets[dist[v]]
                dist[v] = newDist
                buckets[newDist].add(v)

    return dist

import statistics, time

n, m, c, graph = create_graph()
print(fastDijkstra())
# tempos = []
# for _ in range(10):
#     start = time.perf_counter()
#     fastDijkstra()
#     end = time.perf_counter()
#     tempos.append(end - start)

# print("Média:", statistics.mean(tempos))
# print("Mediana:", statistics.median(tempos))
# print("Mínimo:", min(tempos))