# Main source: https://www.naukri.com/code360/library/dials-algorithm

### `graphgen.py`
Gera um grafo conexo com: `n` vértices, `e` arestas, `w` pesos possíveis.

A conexão do grafo é garantida em duas etapas:
1. Criação de uma árvore geradora, conectando todos os vértices.
2. Adição das arestas restantes até atingir o total desejado.

Os pesos são distribuídos de forma uniforme:  
há aproximadamente o mesmo número de arestas de peso `1`, `2`, ..., `w`.

### `dijkstra.py`
Implementação clássica do algoritmo de Dijkstra usando heap binário (priority queue). Complexidade: `O((V+E) log V)`  

### `fastDijkstra.py`
Implementação otimizada baseada no algoritmo de Dial, que utiliza buckets em vez de heap.  
Complexidade: `O(E + V.C)`, onde `C = max{peso}`  