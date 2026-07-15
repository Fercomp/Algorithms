from collections import deque

def predictPartyVictory(senate):
    queue = deque(senate)
    d_count, r_count = 0, 0
    for s in senate:
        if s == "D":
            d_count += 1
        else:
            r_count += 1
    
    
    d_to_delete, r_to_delete = 0, 0
    
    while queue:
        if d_count == 0 or r_count == 0:
            break
        for _ in range(len(queue)):            
            v = queue.popleft()
            
            if v == "D" and not d_to_delete:
                r_to_delete += 1
                queue.append("D")
                
            if v == "D" and d_to_delete:
                d_to_delete -= 1
                d_count -= 1
            
            if v == "R" and not r_to_delete:
                d_to_delete += 1
                queue.append("R")
                
            if v == "R" and r_to_delete:
                r_to_delete -= 1
                r_count -= 1
    
    return "Dire" if d_count > r_count else "Radiant"    

print(predictPartyVictory("RDD"))