import random, utils

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
    file = utils.get_input_file(x)
    
    with open(file, "w") as f:
        # Define um vertice inicial s e um final d
        s = random.randrange(0, n)
        d = utils.rand_exclude(0, n, s)
        f.write(f"{n} {m} {w} {s} {d} \n")
        print(f"Generating Graph {x}, n={n} m={m} w={w} s={s} d={d}")
        
        # Criar uma spanning tree antes de adicionar o resto das arestas
        for u in range(1, n):
            v = random.randrange(0, u)
            f.write(f"{u} {v} {weights[count]}\n")
            edges.add((u, v))
            count += 1
        
        while count < m:
            u = random.randrange(0, n) 
            v = random.randrange(0, n)
            if u != v and (u, v) not in edges:
                line = f"{u} {v} {weights[count]}"
                if count < m - 1:
                    line += "\n"
                f.write(line)
                edges.add((u, v))
                count += 1 

for i in range(1, 16):
    n = random.randrange(1000, 5000)
    m = random.randrange(5 * n, 10 * n)
    c = random.randrange(1, 10)
    generate_balanced_connected_graph(n, m, c, i)