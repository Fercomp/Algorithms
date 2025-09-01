import math, heapq, statistics, time, os

def create_graph(x):
    graph = {}
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    INPUT_DIR = os.path.join(BASE_DIR, "input")
    os.makedirs(INPUT_DIR, exist_ok=True)
    file = os.path.join(INPUT_DIR, f"graph{x}.txt")
    with open(file) as f:
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

tempos = []
for x in range(1, 16):
    graph = create_graph(x)
    start = time.perf_counter()
    dijkstra()
    end = time.perf_counter()
    print(end - start)
    tempos.append(end - start)
    
print("Média:", statistics.mean(tempos))