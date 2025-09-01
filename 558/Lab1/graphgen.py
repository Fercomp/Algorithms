import random
import os

def generate_balanced_connected_graph(n, m, w, x):
    integer, rest = divmod(m, w)
    weights = []
    for i in range(1, w+1):
        weights += integer * [i]
    for i in range(1, rest + 1):
        weights.append(i)
    random.shuffle(weights)
    
    edges = set()
    count = 0
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    INPUT_DIR = os.path.join(BASE_DIR, "input")
    os.makedirs(INPUT_DIR, exist_ok=True)
    file = os.path.join(INPUT_DIR, f"graph{x}.txt")
    with open(file, "w") as f:
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

for i in range(1, 16):
    generate_balanced_connected_graph(10000, 100000, 1000, i)