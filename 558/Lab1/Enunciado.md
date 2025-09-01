Você é um projetista de algoritmos contratado por uma empresa de delivery de comida e precisa implementar um sistema de rotas para os entregadores. Antes de ser implantado globalmente, o algoritmo será testado em uma cidade específica. Nessa cidade, o mapa é modelado como um grafo, em que os vértices representam cruzamentos e as arestas representam ruas. 
Por sorte a empresa de delivery tem um sistema que te retorna o tempo que um motoboy demora para atravessar a rua x em minutos.​ O grafo será fornecido na forma de lista de adjacência, juntamente com um cruzamento de origem 𝑠 s (source) e um cruzamento de destino 𝑑 d (destination). O objetivo é projetar um algoritmo que determine a rota mais rápida entre 𝑠 s e 𝑑 d, considerando o tempo de viagem como critério. Um detalhe importante: o sistema viário da cidade foi planejado de forma balanceada.Dessa forma o número de ruas que demora 2 minutos para se atravessar é muito parecido com o ‘numero de ruas em que se demorar 3 minutos e assim por diante. Essa característica deve te lembrar das aulas da disciplina 448, onde você estudou algoritmos de ordenação em tempo linear. Como você deseja causar uma boa impressão, promete que, sob essas condições, é capaz de projetar um algoritmo mais eficiente que o clássico Dijkstra para resolver o problema de caminhos mínimos.

Input 
A primeira linha de input será 5 números n, m, c, s e d. onde n é o número de vértices, m é o número de arestas, c é o o maior peso w possivél com 1 <= w <= c. s é o vértice de origem, d é o vertice de destino.
As próximas m linhas são as arestas que estarão no formato, u v w. Onde u é vertice origem v é vertice destino e w é o peso.
Exemplo:
3561 24507 9 1487 664 
1 0 7
2 0 8
3 2 9
4 0 1
5 2 9
6 0 3
7 3 4

Output
Apenas um número que signifca a menor distancia de s ara d
Exemplo:
34