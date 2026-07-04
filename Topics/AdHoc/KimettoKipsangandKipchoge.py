while True:
    try:
        n, r = map(int, input().split())
        trees = input().split()
        
        for _ in range(r):
            d = input().split()
            
            if d[0] == "E":
                visited = set()
                distance = 0
                
                for i in range(int(d[1])-1, -1, -1):
                    if trees[i] in visited:
                        break
                    visited.add(trees[i])
                    distance += 1
                    
                print(distance)
                
            else:
                trees[int(d[1])-1] = d[2]
    
    except EOFError:
        break