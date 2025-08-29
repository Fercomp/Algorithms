import random

def generate_balanced_connected_graph(n, m, w):
    integer, rest = divmod(m, w)
    weights = []
    for i in range(1, w+1):
        weights += integer * [i]
    for i in range(1, rest + 1):
        weights.append(i)
    random.shuffle(weights)
    
    edges = set()
    count = 0
    with open("graph.txt", "w") as f:
        f.write(f"{n} {m} {w}\n")
        
        # Criar uma spanning tree antes de adicionar o resto das arestas
        for u in range(1, n):
            v = random.randrange(0, u)
            f.write(f"{u} {v} {weights[count]}\n")
            edges.add((u, v))
            count += 1
        
        while count < m:
            u = random.randrange(0, n) 
            v = random.randrange(0, n)
            if (u, v) not in edges:
                line = f"{u} {v} {weights[count]}"
                if count < m - 1:
                    line += "\n"
                f.write(line)
                edges.add((u, v))
                count += 1 
    
generate_balanced_connected_graph(1000, 5000, 500)