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
    

def shortestPath(s=0):
    n, m, c, graph = create_graph()
    dist = [sys.maxsize] * len(graph)
    dist[s] = 0
    
    maxDist = (n - 1) * c
    buckets = defaultdict(set)
    buckets[0].add(s)
    
    # Process buckets in order
    for d in range(maxDist + 1):
        # Process all nodes in current bucket
        while d in buckets and buckets[d]:
            u = buckets[d].pop()
            
            # Skip if we already found a better path
            if d > dist[u]:
                continue
            
            # Process all adjacent nodes
            for edge in graph[u]:
                v, weight = edge[0], edge[1]
                newDist = dist[u] + weight
                
                # If shorter path found
                if newDist < dist[v]:
                    # Remove from old bucket if it was there
                    if dist[v] != sys.maxsize:
                        buckets[dist[v]].discard(v)
                    
                    # Update distance and add to new bucket
                    dist[v] = newDist
                    buckets[newDist].add(v)
    
    return dist

def dijkstra_dial(s=0):
    n, m, c, graph = create_graph()
    dist = [sys.maxsize] * n
    dist[s] = 0
    maxDist = (n - 1) * c
    buckets = [[] for _ in range(maxDist + 1)]
    buckets[0].append(s)
    
    idx = 0
    while idx <= maxDist:
        while buckets[idx]:
            u = buckets[idx].pop()
            if dist[u] < idx:
                continue
            for v, w in graph[u]:
                newDist = dist[u] + w
                if newDist < dist[v]:
                    dist[v] = newDist
                    buckets[newDist].append(v)
        idx += 1
    
    return dist

def please(s=0):
    n, m, c, graph = create_graph()
    dist = [sys.maxsize] * len(graph)
    dist[s] = 0

    maxDist = (n - 1) * c
    buckets = defaultdict(set)
    buckets[0].add(s)
    
    bucket_pointer = 0
    while buckets:
        # Pega o bucket com menor distância não vazio
        while bucket_pointer not in buckets or not buckets[bucket_pointer]:
            bucket_pointer += 1
            if bucket_pointer > maxDist:
                break
        if bucket_pointer > maxDist:
            break
        
        u = buckets[bucket_pointer].pop()
        if not buckets[bucket_pointer]:
            del buckets[bucket_pointer]

        for v, w in graph[u]:
            newDist = dist[u] + w
            if newDist < dist[v]:
                if dist[v] != sys.maxsize:
                    buckets[dist[v]].discard(v)
                    if not buckets[dist[v]]:
                        del buckets[dist[v]]
                dist[v] = newDist
                buckets[newDist].add(v)

    return dist

inicio = time.time()
for _ in range(100):
    please()
fim = time.time()
print("Tempo de execução:", fim - inicio, "segundos")