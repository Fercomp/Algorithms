import random

def generate_balanced_connected_graph(n, m, weights=[1,2,3,4], filename=None):
    """
    Gera um grafo direcionado, conexo, com n nós e m arestas.
    Os pesos são divididos igualmente entre os valores em 'weights'.
    Se filename for passado, o grafo será salvo em um arquivo txt.
    """
    if m < n - 1:
        raise ValueError("Precisa de pelo menos n-1 arestas para manter o grafo conexo.")

    graph = {i: [] for i in range(n)}
    all_edges = set()  # conjunto para evitar arestas repetidas

    # --- Passo 1: cria uma árvore direcionada para garantir conectividade
    for i in range(1, n):
        u = i
        v = random.randint(0, i - 1)  # conecta com algum nó anterior
        w = random.choice(weights)
        all_edges.add((u, v, w))
        graph[u].append((v, w))

    edges_used = n - 1
    remaining_edges = m - edges_used

    # --- Passo 2: distribui os pesos igualmente no resto das arestas
    per_weight = remaining_edges // len(weights)

    for w in weights:
        for _ in range(per_weight):
            while True:
                u = random.randint(0, n - 1)
                v = random.randint(0, n - 1)
                if u != v and (u, v, w) not in all_edges:
                    break
            all_edges.add((u, v, w))
            graph[u].append((v, w))

    # se faltar algumas arestas por conta da divisão inteira, completa aleatório
    while len(all_edges) < m:
        w = random.choice(weights)
        while True:
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            if u != v and (u, v, w) not in all_edges:
                break
        all_edges.add((u, v, w))
        graph[u].append((v, w))

    # --- Passo 3: salvar no arquivo, se filename for passado
    if filename:
        with open(filename, "w") as f:
            f.write(str(len(all_edges)) + "\n")
            for u, v, w in all_edges:
                f.write(f"{u} {v} {w}\n")

    return graph
