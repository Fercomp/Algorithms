import math
import heapq

# Edges are given as a list of triples [u, v, w]
# u = starting vertex, v = ending vertex, w = edge weight
edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]] 

def create_graph(edges):
    """
    Convert edge list into an adjacency list representation.
    Each vertex maps to a list of (weight, neighbor) pairs.
    Since this example is undirected, we add both directions.
    """
    graph = {}
    for u, v, w in edges:
        graph.setdefault(u, []).append((w, v))
        graph.setdefault(v, []).append((w, u))
    return graph

def dijkstra(edges, s=0):
    """
    Compute shortest paths from source vertex `s` using Dijkstra's algorithm.
    Returns an array where dist[i] is the minimum distance from s to i.
    """
    graph = create_graph(edges)

    # Initialize all distances as infinity
    dist = [math.inf] * len(graph)
    dist[s] = 0  # Distance to source is 0

    # Priority queue stores (distance, vertex) pairs
    heap = [(0, s)]
    
    while heap:
        # Pop the vertex with the smallest known distance
        d, v = heapq.heappop(heap)

        # If this distance is outdated, skip it
        if d > dist[v]:
            continue

        # Relax edges
        for w, u in graph[v]:
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                heapq.heappush(heap, (dist[u], u))

    return dist

print(dijkstra(edges))