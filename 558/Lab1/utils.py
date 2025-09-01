import random, os 
from collections import defaultdict

def rand_exclude(start, stop, exclude):
    x = random.randrange(start, stop)
    while x == exclude:
        x = random.randrange(start, stop)
    return x

def get_input_file(x):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    INPUT_DIR = os.path.join(BASE_DIR, "input")
    os.makedirs(INPUT_DIR, exist_ok=True)
    file = os.path.join(INPUT_DIR, f"graph{x}.txt")
    return file

def create_graph(x):
    graph = defaultdict(list)
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    INPUT_DIR = os.path.join(BASE_DIR, "input")
    os.makedirs(INPUT_DIR, exist_ok=True)
    file = os.path.join(INPUT_DIR, f"graph{x}.txt")
    
    with open(file) as f:
        n, m, c, s, d = map(int, f.readline().split())
        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            graph[u].append((w, v))
    return n, m, c, s, d, graph