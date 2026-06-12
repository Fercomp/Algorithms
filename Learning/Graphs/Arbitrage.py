case = 0
while True:
    
    try:
        line = input().strip()
    except:
        break
        
    if not line:
        continue
        
    n = int(line)
    if n == 0:
        break
    case += 1

    currency_to_index = {}
    for i in range(n):
        currency = input()
        currency_to_index[currency] = i

    graph = [[0.0] * (n) for _ in range(n)]

    for i in range(n):
        graph[i][i] = 1

    str = input().strip()
    while not str:
        str = input().strip()
    m = int(str)

    for i in range(m):
        a, w, b = input().split()
        graph[currency_to_index[a]][currency_to_index[b]] = float(w)

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                graph[i][j] = max(graph[i][j], graph[i][k] * graph[k][j])

    has_arbitrage = False     
    for i in range(n):
        if graph[i][i] > 1:
            has_arbitrage = True
            break

    print(f"Case {case}: {'Yes' if has_arbitrage else 'No'}")