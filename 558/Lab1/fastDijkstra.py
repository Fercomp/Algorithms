import sys, statistics, time, utils
from collections import defaultdict

def fastDijkstra(n, source, destination, graph):
    dist = [sys.maxsize] * n
    dist[source] = 0

    maxDist = (n - 1) * c
    buckets = defaultdict(set)
    buckets[0].add(source)
    
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
    
    return dist[destination]

tempos = []
for x in range(1, 16):
    n, m, c, s, d, graph = utils.create_graph(x)
    start = time.perf_counter()
    fastDijkstra(n, s, d, graph)
    end = time.perf_counter()
    interval = end - start
    print(f"Fast Dijkstra n={n}, m={m}, c={c}, s={s}, d={d}, time={interval}")
    tempos.append(interval)

print("Média:", statistics.mean(tempos))